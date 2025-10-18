import { useState } from 'react'
import FileUpload from './components/FileUpload'
import ConfigForm from './components/ConfigForm'
import ImageList from './components/ImageList'
import type { UploadConfig } from './services/uploadService'
import './App.css'

function App() {
  const [uploadConfig, setUploadConfig] = useState<UploadConfig>({
    baseUrl: 'http://0.0.0.0:3000',
    accessToken: '',
    osId: 1,
    osType: 'task_item',
  })

  const [uploadStatus, setUploadStatus] = useState<string>('')
  const [refreshTrigger, setRefreshTrigger] = useState<number>(0)

  const handleConfigChange = (newConfig: UploadConfig) => {
    setUploadConfig(newConfig)
    setUploadStatus('Configuration updated successfully!')
    setTimeout(() => setUploadStatus(''), 3000)
  }

  const handleUploadComplete = (response: any) => {
    console.log('Upload completed:', response)
    setUploadStatus('Files uploaded successfully!')
    setRefreshTrigger(prev => prev + 1) // Trigger refresh of file list
    setTimeout(() => setUploadStatus(''), 5000)
  }

  const handleUploadError = (error: string) => {
    console.error('Upload error:', error)
    setUploadStatus(`Upload failed: ${error}`)
    setTimeout(() => setUploadStatus(''), 5000)
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>📁 File Upload System</h1>
        <p>Upload images and documents with custom labels</p>
      </header>

      <main className="app-main">
        <div className="main-container">
          <ConfigForm
            onConfigChange={handleConfigChange}
            initialConfig={uploadConfig}
          />

          {uploadStatus && (
            <div className={`status-message ${uploadStatus.includes('failed') ? 'error' : 'success'}`}>
              {uploadStatus}
            </div>
          )}

          <FileUpload
            uploadConfig={uploadConfig}
            onUploadComplete={handleUploadComplete}
            onUploadError={handleUploadError}
            maxFiles={10}
            maxSize={10 * 1024 * 1024} // 10MB
          />

          <ImageList
            uploadConfig={uploadConfig}
            refreshTrigger={refreshTrigger}
          />
        </div>
      </main>

      <footer className="app-footer">
        <p>Built with React + TypeScript + react-dropzone</p>
      </footer>
    </div>
  )
}

export default App

