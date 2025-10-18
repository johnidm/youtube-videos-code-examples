import React, { useCallback, useState } from 'react';
import { useDropzone, type FileRejection } from 'react-dropzone';
import { UploadService, type FileWithLabel, type UploadConfig } from '../services/uploadService';
import './FileUpload.css';

interface FileUploadProps {
  uploadConfig: UploadConfig;
  onUploadComplete?: (response: any) => void;
  onUploadError?: (error: string) => void;
  maxFiles?: number;
  maxSize?: number;
}

interface FileItem extends FileWithLabel {
  id: string;
}

const FileUpload: React.FC<FileUploadProps> = ({
  uploadConfig,
  onUploadComplete,
  onUploadError,
  maxFiles = 10,
  maxSize = 10 * 1024 * 1024, // 10MB
}) => {
  const [files, setFiles] = useState<FileItem[]>([]);
  const [uploadError, setUploadError] = useState<string | null>(null);
  const [isUploading, setIsUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState<number>(0);

  const uploadService = new UploadService(uploadConfig);

  const onDropAccepted = useCallback((acceptedFiles: File[]) => {
    const newFiles: FileItem[] = acceptedFiles.map((file) => ({
      id: `${file.name}-${Date.now()}-${Math.random()}`,
      file,
      label: '', // User will fill this in
    }));
    
    setFiles(prev => [...prev, ...newFiles]);
    setUploadError(null);
  }, []);

  const onDropRejected = useCallback((fileRejections: FileRejection[]) => {
    const errors = fileRejections.map(
      (rejection) => `${rejection.file.name}: ${rejection.errors[0].message}`
    );
    setUploadError(errors.join('\n'));
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDropAccepted,
    onDropRejected,
    maxFiles,
    maxSize,
    accept: {
      'image/*': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.webp'],
      'text/plain': ['.txt'],
      'application/pdf': ['.pdf'],
    },
    multiple: true,
  });

  const updateFileLabel = (fileId: string, label: string) => {
    setFiles(prev => 
      prev.map(file => 
        file.id === fileId ? { ...file, label } : file
      )
    );
  };

  const removeFile = (fileId: string) => {
    setFiles(prev => prev.filter(file => file.id !== fileId));
  };

  const handleUpload = async () => {
    if (files.length === 0) {
      setUploadError('Please select at least one file');
      return;
    }

    const filesWithoutLabels = files.filter(file => !file.label.trim());
    if (filesWithoutLabels.length > 0) {
      setUploadError('Please provide labels for all files');
      return;
    }

    setIsUploading(true);
    setUploadProgress(0);
    setUploadError(null);

    try {
      // Simulate progress for better UX
      const progressInterval = setInterval(() => {
        setUploadProgress(prev => Math.min(prev + 10, 90));
      }, 200);

      const response = await uploadService.uploadFiles(files);
      
      clearInterval(progressInterval);
      setUploadProgress(100);

      if (response.success) {
        onUploadComplete?.(response.data);
        setFiles([]);
        setTimeout(() => {
          setUploadProgress(0);
          setIsUploading(false);
        }, 1000);
      } else {
        throw new Error(response.message || 'Upload failed');
      }
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Upload failed';
      setUploadError(errorMessage);
      onUploadError?.(errorMessage);
      setUploadProgress(0);
      setIsUploading(false);
    }
  };

  const formatFileSize = (bytes: number): string => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  return (
    <div className="file-upload-container">
      <div className="upload-header">
        <h2>Upload Files</h2>
        <p>Supported types: Images (JPEG, PNG, GIF, etc.), Text files, PDF</p>
      </div>

      <div
        {...getRootProps()}
        className={`dropzone ${isDragActive ? 'active' : ''} ${isUploading ? 'disabled' : ''}`}
      >
        <input {...getInputProps()} disabled={isUploading} />
        <div className="dropzone-content">
          <div className="upload-icon">📁</div>
          {isDragActive ? (
            <p>Drop the files here...</p>
          ) : (
            <>
              <p>Drag and drop files here, or <span className="click-text">click to select</span></p>
              <p className="upload-limits">
                Max {maxFiles} files, {formatFileSize(maxSize)} per file
              </p>
            </>
          )}
        </div>
      </div>

      {uploadError && (
        <div className="error-message">
          <span className="error-icon">⚠️</span>
          <pre>{uploadError}</pre>
        </div>
      )}

      {files.length > 0 && (
        <div className="file-list">
          <h3>Selected Files ({files.length})</h3>
          <div className="files-grid">
            {files.map((fileItem) => (
              <div key={fileItem.id} className="file-item">
                <div className="file-info">
                  <div className="file-name">{fileItem.file.name}</div>
                  <div className="file-size">{formatFileSize(fileItem.file.size)}</div>
                </div>
                <div className="file-label">
                  <label htmlFor={`label-${fileItem.id}`}>Label:</label>
                  <input
                    id={`label-${fileItem.id}`}
                    type="text"
                    value={fileItem.label}
                    onChange={(e) => updateFileLabel(fileItem.id, e.target.value)}
                    placeholder="Enter file description..."
                    disabled={isUploading}
                  />
                </div>
                <button
                  type="button"
                  onClick={() => removeFile(fileItem.id)}
                  className="remove-file-btn"
                  disabled={isUploading}
                  aria-label={`Remove ${fileItem.file.name}`}
                >
                  ✕
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      {files.length > 0 && (
        <div className="upload-actions">
          <button
            type="button"
            onClick={handleUpload}
            disabled={isUploading || files.length === 0}
            className="upload-btn"
          >
            {isUploading ? 'Uploading...' : `Upload ${files.length} file${files.length > 1 ? 's' : ''}`}
          </button>
          
          {!isUploading && (
            <button
              type="button"
              onClick={() => setFiles([])}
              className="clear-btn"
            >
              Clear All
            </button>
          )}
        </div>
      )}

      {isUploading && (
        <div className="upload-progress">
          <div className="progress-bar">
            <div 
              className="progress-fill" 
              style={{ width: `${uploadProgress}%` }}
            ></div>
          </div>
          <div className="progress-text">{uploadProgress}%</div>
        </div>
      )}
    </div>
  );
};

export default FileUpload;
