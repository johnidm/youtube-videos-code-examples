export interface FileWithLabel {
  file: File;
  label: string;
}

export interface UploadConfig {
  baseUrl: string;
  accessToken: string;
  osId: number;
  osType: 'supplier' | 'task_item' | 'corrective' | 'preventive';
}

export interface UploadResponse {
  success: boolean;
  message?: string;
  data?: any;
}

export interface FileItem {
  id: string;
  filename: string;
  originalName: string;
  mimeType?: string;
  size: number;
  label?: string;
  url?: string;
  createdAt: string;
  updatedAt: string;
}

export interface FetchFilesResponse {
  success: boolean;
  message?: string;
  data?: FileItem[];
}

export class UploadService {
  private config: UploadConfig;

  constructor(config: UploadConfig) {
    this.config = config;
  }

  async uploadFiles(filesWithLabels: FileWithLabel[]): Promise<UploadResponse> {
    const formData = new FormData();

    // Add files and labels according to the API specification
    filesWithLabels.forEach(({ file, label }) => {
      formData.append('files', file);
      formData.append('labels', label);
    });

    try {
      const response = await fetch(
        `${this.config.baseUrl}/api/files/${this.config.osId}/bulk/${this.config.osType}`,
        {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${this.config.accessToken}`,
          },
          body: formData,
        }
      );

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.message || `Upload failed with status: ${response.status}`);
      }

      const result = await response.json();
      return {
        success: true,
        data: result,
      };
    } catch (error) {
      console.error('Upload error:', error);
      return {
        success: false,
        message: error instanceof Error ? error.message : 'Upload failed',
      };
    }
  }

  async fetchFiles(): Promise<FetchFilesResponse> {
    try {
      const response = await fetch(
        `${this.config.baseUrl}/api/files?osId=${this.config.osId}&osType=${this.config.osType}`,
        {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${this.config.accessToken}`,
            'Content-Type': 'application/json',
          },
        }
      );

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.message || `Failed to fetch files: ${response.status}`);
      }

      const result = await response.json();
      return {
        success: true,
        data: result.data || result, // Handle different response structures
      };
    } catch (error) {
      console.error('Fetch files error:', error);
      return {
        success: false,
        message: error instanceof Error ? error.message : 'Failed to fetch files',
      };
    }
  }

  updateConfig(newConfig: Partial<UploadConfig>) {
    this.config = { ...this.config, ...newConfig };
  }
}
