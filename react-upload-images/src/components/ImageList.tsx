import React, { useState, useEffect, useCallback } from 'react';
import { UploadService, type FileItem, type UploadConfig } from '../services/uploadService';
import './ImageList.css';

interface ImageListProps {
  uploadConfig: UploadConfig;
  refreshTrigger?: number; // Used to trigger refresh after uploads
}

const ImageList: React.FC<ImageListProps> = ({ uploadConfig, refreshTrigger }) => {
  const [files, setFiles] = useState<FileItem[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [selectedImage, setSelectedImage] = useState<FileItem | null>(null);

  const uploadService = new UploadService(uploadConfig);

  const fetchFiles = useCallback(async () => {
    if (!uploadConfig.accessToken) {
      setError('Please configure API settings first');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await uploadService.fetchFiles();
      
      if (response.success && response.data) {
        console.log('Fetched files:', response.data); // Debug log
        setFiles(response.data);
      } else {
        throw new Error(response.message || 'Failed to fetch files');
      }
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Failed to fetch files';
      setError(errorMessage);
      console.error('Error fetching files:', err);
    } finally {
      setLoading(false);
    }
  }, [uploadConfig]);

  useEffect(() => {
    fetchFiles();
  }, [fetchFiles, refreshTrigger]);

  const isImageFile = (mimeType: string | undefined | null): boolean => {
    return mimeType ? mimeType.startsWith('image/') : false;
  };

  const formatFileSize = (bytes: number | undefined): string => {
    if (!bytes || bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  const formatDate = (dateString: string): string => {
    try {
      return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
      });
    } catch {
      return dateString;
    }
  };

  const getFileIcon = (mimeType: string | undefined | null): string => {
    if (!mimeType) return '📎';
    if (mimeType.startsWith('image/')) return '🖼️';
    if (mimeType === 'application/pdf') return '📄';
    if (mimeType.startsWith('text/')) return '📝';
    return '📎';
  };

  const openImageModal = (file: FileItem) => {
    if (isImageFile(file.mimeType)) {
      setSelectedImage(file);
    }
  };

  const closeImageModal = () => {
    setSelectedImage(null);
  };

  if (loading) {
    return (
      <div className="image-list-container">
        <div className="image-list-header">
          <h2>📁 Files</h2>
          <button onClick={fetchFiles} className="refresh-btn" disabled>
            🔄 Refreshing...
          </button>
        </div>
        <div className="loading-state">
          <div className="loading-spinner"></div>
          <p>Loading files...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="image-list-container">
        <div className="image-list-header">
          <h2>📁 Files</h2>
          <button onClick={fetchFiles} className="refresh-btn">
            🔄 Refresh
          </button>
        </div>
        <div className="error-state">
          <span className="error-icon">⚠️</span>
          <p>{error}</p>
          <button onClick={fetchFiles} className="retry-btn">
            Try Again
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="image-list-container">
      <div className="image-list-header">
        <h2>📁 Files ({files.length})</h2>
        <button onClick={fetchFiles} className="refresh-btn">
          🔄 Refresh
        </button>
      </div>

      {files.length === 0 ? (
        <div className="empty-state">
          <div className="empty-icon">📂</div>
          <h3>No files found</h3>
          <p>Upload some files to see them here</p>
        </div>
      ) : (
        <div className="files-grid">
          {files.map((file) => (
            <div
              key={file.id}
              className={`file-card ${isImageFile(file.mimeType) ? 'image-file' : 'document-file'}`}
              onClick={() => openImageModal(file)}
            >
              <div className="file-preview">
                {isImageFile(file.mimeType) && file.url ? (
                  <img
                    src={file.url}
                    alt={file.originalName}
                    className="file-thumbnail"
                    onError={(e) => {
                      const target = e.target as HTMLImageElement;
                      target.style.display = 'none';
                      target.nextElementSibling?.classList.remove('hidden');
                    }}
                  />
                ) : null}
                <div className={`file-icon ${isImageFile(file.mimeType) && file.url ? 'hidden' : ''}`}>
                  {getFileIcon(file.mimeType)}
                </div>
              </div>

              <div className="file-info">
                <h4 className="file-name" title={file.originalName}>
                  {file.originalName}
                </h4>
                
                {file.label && (
                  <p className="file-label" title={file.label}>
                    {file.label}
                  </p>
                )}

                <div className="file-meta">
                  <span className="file-size">{formatFileSize(file.size)}</span>
                  <span className="file-date">{formatDate(file.createdAt)}</span>
                </div>

                <div className="file-type">
                  {file.mimeType || 'Unknown type'}
                </div>
              </div>

              {isImageFile(file.mimeType) && (
                <div className="image-overlay">
                  <span>👁️ View</span>
                </div>
              )}
            </div>
          ))}
        </div>
      )}

      {/* Image Modal */}
      {selectedImage && (
        <div className="image-modal" onClick={closeImageModal}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <button className="modal-close" onClick={closeImageModal}>
              ✕
            </button>
            <div className="modal-header">
              <h3>{selectedImage.originalName}</h3>
              {selectedImage.label && <p className="modal-label">{selectedImage.label}</p>}
            </div>
            <div className="modal-image-container">
              {selectedImage.url ? (
                <img
                  src={selectedImage.url}
                  alt={selectedImage.originalName}
                  className="modal-image"
                />
              ) : (
                <div className="modal-no-preview">
                  <span>🖼️</span>
                  <p>Image preview not available</p>
                </div>
              )}
            </div>
            <div className="modal-footer">
              <div className="modal-meta">
                <span>Size: {formatFileSize(selectedImage.size)}</span>
                <span>Type: {selectedImage.mimeType || 'Unknown'}</span>
                <span>Uploaded: {formatDate(selectedImage.createdAt)}</span>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ImageList;
