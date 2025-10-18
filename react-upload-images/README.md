# 📁 File Upload System

A modern React application for uploading files with drag-and-drop functionality, built with TypeScript and Vite. This application implements a multipart/form-data upload system that matches a specific API specification.

## ✨ Features

- **Drag & Drop Interface**: Intuitive file selection with drag-and-drop support
- **Multiple File Upload**: Upload multiple files simultaneously with individual labels
- **File Validation**: Automatic validation for file types and sizes
- **Progress Tracking**: Real-time upload progress with visual feedback
- **File Gallery**: View and browse uploaded files with image previews
- **Image Modal**: Full-screen image preview with metadata
- **Auto-refresh**: File list automatically updates after uploads
- **Responsive Design**: Modern, mobile-friendly interface
- **TypeScript**: Full type safety and excellent developer experience
- **API Configuration**: Configurable endpoint settings for different environments

## 🚀 Supported File Types

- **Images**: JPEG, JPG, PNG, GIF, BMP, WebP
- **Documents**: PDF, TXT
- **Custom**: Easily extensible for additional file types

## 🛠️ Technology Stack

- **React 19** with TypeScript
- **Vite** for fast development and building
- **react-dropzone** for drag-and-drop functionality
- **Modern CSS** with responsive design
- **Fetch API** for HTTP requests

## 📋 API Specification

The application uploads files to an endpoint with the following specification:

```
POST {{baseUrl}}/api/files/{{osId}}/bulk/{{osType}}
Authorization: Bearer {{accessToken}}
Content-Type: multipart/form-data
```

**Supported OS Types:**
- `supplier`
- `task_item`
- `corrective`
- `preventive`

**Form Data Structure:**
- `files`: The actual file data
- `labels`: Corresponding labels for each file

### File Listing API

The application also fetches and displays files using:

```
GET {{baseUrl}}/api/files?osId={{osId}}&osType={{osType}}
Authorization: Bearer {{accessToken}}
Content-Type: application/json
```

**Expected Response Format:**
```json
{
  "data": [
    {
      "id": "string",
      "filename": "string",
      "originalName": "string",
      "mimeType": "string",
      "size": number,
      "label": "string",
      "url": "string",
      "createdAt": "string",
      "updatedAt": "string"
    }
  ]
}
```

## 🚀 Getting Started

### Prerequisites

- Node.js 20.19+ or 22.12+
- npm or yarn

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd react-upload-images
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   Navigate to `http://localhost:5173`

### Building for Production

```bash
npm run build
```

## 🎯 Usage

1. **Configure API Settings**
   - Click the "⚙️ API Configuration" button
   - Enter your API base URL, access token, OS ID, and OS type
   - Save the configuration

2. **Upload Files**
   - Drag and drop files into the upload area, or click to select files
   - Add descriptive labels for each file
   - Click "Upload" to send files to your API

3. **View Files**
   - Browse uploaded files in the gallery below the upload area
   - Click on images to view them in full-screen modal
   - Use the refresh button to manually update the file list

4. **Monitor Progress**
   - Watch the real-time upload progress
   - Receive success/error feedback
   - File list automatically refreshes after successful uploads

## 📁 Project Structure

```
src/
├── components/
│   ├── FileUpload.tsx      # Main upload component
│   ├── FileUpload.css      # Upload component styles
│   ├── ConfigForm.tsx      # API configuration form
│   ├── ConfigForm.css      # Configuration form styles
│   ├── ImageList.tsx       # File gallery component
│   └── ImageList.css       # Gallery component styles
├── services/
│   └── uploadService.ts    # API service for uploads and file fetching
├── App.tsx                 # Main application component
├── App.css                 # Global application styles
└── main.tsx               # Application entry point
```

## 🔧 Configuration Options

### FileUpload Component Props

- `uploadConfig`: API configuration object
- `onUploadComplete`: Callback for successful uploads
- `onUploadError`: Callback for upload errors
- `maxFiles`: Maximum number of files (default: 10)
- `maxSize`: Maximum file size in bytes (default: 10MB)

### ImageList Component Props

- `uploadConfig`: API configuration object
- `refreshTrigger`: Number that triggers a refresh when changed

## 🎨 Customization

### Styling
The application uses modern CSS with CSS custom properties. You can easily customize colors, spacing, and animations by modifying the CSS files.

### File Types
To add support for additional file types, update the `accept` object in the `useDropzone` configuration:

```typescript
accept: {
  'image/*': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.webp'],
  'text/plain': ['.txt'],
  'application/pdf': ['.pdf'],
  // Add more types here
}
```

## 🔒 Security Considerations

- Never hardcode API tokens in the source code
- Use environment variables for sensitive configuration
- Implement proper server-side validation
- Consider file size limits and virus scanning

## 🐛 Troubleshooting

### Common Issues

1. **CORS Errors**: Ensure your API server allows requests from your domain
2. **File Size Limits**: Check both client-side and server-side file size limits
3. **Authentication**: Verify your access token is valid and has proper permissions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:

```js
export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...

      // Remove tseslint.configs.recommended and replace with this
      tseslint.configs.recommendedTypeChecked,
      // Alternatively, use this for stricter rules
      tseslint.configs.strictTypeChecked,
      // Optionally, add this for stylistic rules
      tseslint.configs.stylisticTypeChecked,

      // Other configs...
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from 'eslint-plugin-react-x'
import reactDom from 'eslint-plugin-react-dom'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...
      // Enable lint rules for React
      reactX.configs['recommended-typescript'],
      // Enable lint rules for React DOM
      reactDom.configs.recommended,
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```
