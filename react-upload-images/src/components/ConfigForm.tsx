import React, { useState } from 'react';
import type { UploadConfig } from '../services/uploadService';
import './ConfigForm.css';

interface ConfigFormProps {
  onConfigChange: (config: UploadConfig) => void;
  initialConfig?: Partial<UploadConfig>;
}

const ConfigForm: React.FC<ConfigFormProps> = ({ onConfigChange, initialConfig }) => {
  const [config, setConfig] = useState<UploadConfig>({
    baseUrl: initialConfig?.baseUrl || 'https://api.example.com',
    accessToken: initialConfig?.accessToken || '',
    osId: initialConfig?.osId || 1,
    osType: initialConfig?.osType || 'task_item',
  });

  const [isExpanded, setIsExpanded] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onConfigChange(config);
  };

  const handleInputChange = (field: keyof UploadConfig, value: string | number) => {
    const updatedConfig = { ...config, [field]: value };
    setConfig(updatedConfig);
  };

  return (
    <div className="config-form-container">
      <button
        type="button"
        onClick={() => setIsExpanded(!isExpanded)}
        className="config-toggle"
      >
        ⚙️ API Configuration {isExpanded ? '▼' : '▶'}
      </button>
      
      {isExpanded && (
        <form onSubmit={handleSubmit} className="config-form">
          <div className="form-grid">
            <div className="form-group">
              <label htmlFor="baseUrl">Base URL</label>
              <input
                id="baseUrl"
                type="url"
                value={config.baseUrl}
                onChange={(e) => handleInputChange('baseUrl', e.target.value)}
                placeholder="https://api.example.com"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="accessToken">Access Token</label>
              <input
                id="accessToken"
                type="password"
                value={config.accessToken}
                onChange={(e) => handleInputChange('accessToken', e.target.value)}
                placeholder="Bearer token"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="osId">OS ID</label>
              <input
                id="osId"
                type="number"
                value={config.osId}
                onChange={(e) => handleInputChange('osId', parseInt(e.target.value) || 1)}
                min="1"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="osType">OS Type</label>
              <select
                id="osType"
                value={config.osType}
                onChange={(e) => handleInputChange('osType', e.target.value as UploadConfig['osType'])}
                required
              >
                <option value="supplier">Supplier</option>
                <option value="task_item">Task Item</option>
                <option value="corrective">Corrective</option>
                <option value="preventive">Preventive</option>
              </select>
            </div>
          </div>

          <button type="submit" className="config-save-btn">
            Save Configuration
          </button>
        </form>
      )}
    </div>
  );
};

export default ConfigForm;
