import { useState } from 'react'
import { Upload, AlertCircle, CheckCircle, FileText, Camera, Zap } from 'lucide-react'
import './App.css'

export default function App() {
  const [imageFile, setImageFile] = useState(null)
  const [csvFile, setCsvFile] = useState(null)
  const [imagePreview, setImagePreview] = useState(null)
  const [csvPreview, setCsvPreview] = useState(null)
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [activeTab, setActiveTab] = useState('both')

const API_URL = 'https://aryandhanuka10-early-detection.hf.space'

  const handleImageChange = (e) => {
    const file = e.target.files[0]
    if (file) {
      setImageFile(file)
      const reader = new FileReader()
      reader.onload = (event) => setImagePreview(event.target.result)
      reader.readAsDataURL(file)
      setError(null)
    }
  }

  const handleCsvChange = (e) => {
    const file = e.target.files[0]
    if (file) {
      setCsvFile(file)
      const reader = new FileReader()
      reader.onload = (event) => {
        const preview = event.target.result.split('\n').slice(0, 5).join('\n')
        setCsvPreview(preview)
      }
      reader.readAsText(file)
      setError(null)
    }
  }

  const handlePredict = async () => {
    if (!imageFile && !csvFile) {
      setError('Please upload at least an image or CSV file')
      return
    }

    if (activeTab === 'both' && (!imageFile || !csvFile)) {
      setError('For hybrid analysis, please upload both image and CSV')
      return
    }

    setLoading(true)
    setError(null)

    try {
      const formData = new FormData()
      if (imageFile) formData.append('image', imageFile)
      if (csvFile) formData.append('sensor_data', csvFile)
      formData.append('mode', activeTab)

      const response = await fetch(`${API_URL}/predict`, {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || `Prediction failed: ${response.statusText}`)
      }

      const data = await response.json()
      setResults(data)
    } catch (err) {
      setError(err.message || 'Failed to get prediction')
      console.error('Error:', err)
    } finally {
      setLoading(false)
    }
  }

  const getRiskColor = (score) => {
    if (score < 0.33) return 'bg-green-100 border-green-300'
    if (score < 0.67) return 'bg-yellow-100 border-yellow-300'
    return 'bg-red-100 border-red-300'
  }

  const getRiskTextColor = (score) => {
    if (score < 0.33) return 'text-green-700'
    if (score < 0.67) return 'text-yellow-700'
    return 'text-red-700'
  }

  const getRiskLabel = (score) => {
    if (score < 0.33) return 'LOW RISK'
    if (score < 0.67) return 'MEDIUM RISK'
    return 'HIGH RISK'
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-3 mb-4">
            <Zap className="w-8 h-8 text-blue-400" />
            <h1 className="text-4xl font-bold text-white">Manufacturing Quality AI</h1>
          </div>
          <p className="text-slate-300">Early detection of manufacturing defects using Hybrid AI</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Input Panel */}
          <div className="lg:col-span-1">
            <div className="bg-slate-800 rounded-lg border border-slate-700 p-6 sticky top-6">
              <h2 className="text-xl font-bold text-white mb-4">Analysis Mode</h2>

              {/* Mode Selection */}
              <div className="space-y-2 mb-6">
                <label className="flex items-center p-3 bg-slate-700 rounded cursor-pointer hover:bg-slate-600 transition">
                  <input
                    type="radio"
                    name="mode"
                    value="both"
                    checked={activeTab === 'both'}
                    onChange={(e) => setActiveTab(e.target.value)}
                    className="w-4 h-4"
                  />
                  <span className="ml-3 text-white font-medium">Hybrid (Image + Sensor)</span>
                </label>
                <label className="flex items-center p-3 bg-slate-700 rounded cursor-pointer hover:bg-slate-600 transition">
                  <input
                    type="radio"
                    name="mode"
                    value="image"
                    checked={activeTab === 'image'}
                    onChange={(e) => setActiveTab(e.target.value)}
                    className="w-4 h-4"
                  />
                  <span className="ml-3 text-white font-medium">Vision Only</span>
                </label>
                <label className="flex items-center p-3 bg-slate-700 rounded cursor-pointer hover:bg-slate-600 transition">
                  <input
                    type="radio"
                    name="mode"
                    value="sensor"
                    checked={activeTab === 'sensor'}
                    onChange={(e) => setActiveTab(e.target.value)}
                    className="w-4 h-4"
                  />
                  <span className="ml-3 text-white font-medium">Sensor Only</span>
                </label>
              </div>

              <div className="border-t border-slate-700 pt-6">
                {/* Image Upload */}
                {(activeTab === 'both' || activeTab === 'image') && (
                  <div className="mb-6">
                    <label className="block text-sm font-semibold text-white mb-3">
                      <Camera className="w-4 h-4 inline mr-2" />
                      Product Image
                    </label>
                    <label className="block border-2 border-dashed border-slate-600 rounded-lg p-4 cursor-pointer hover:border-blue-400 transition bg-slate-700/50">
                      <input
                        type="file"
                        accept="image/*"
                        onChange={handleImageChange}
                        className="hidden"
                      />
                      <Upload className="w-6 h-6 mx-auto mb-2 text-slate-400" />
                      <p className="text-center text-slate-300 text-sm">
                        {imageFile ? imageFile.name : 'Click to upload image'}
                      </p>
                    </label>
                  </div>
                )}

                {/* CSV Upload */}
                {(activeTab === 'both' || activeTab === 'sensor') && (
                  <div className="mb-6">
                    <label className="block text-sm font-semibold text-white mb-3">
                      <FileText className="w-4 h-4 inline mr-2" />
                      Sensor Data (CSV)
                    </label>
                    <label className="block border-2 border-dashed border-slate-600 rounded-lg p-4 cursor-pointer hover:border-blue-400 transition bg-slate-700/50">
                      <input
                        type="file"
                        accept=".csv"
                        onChange={handleCsvChange}
                        className="hidden"
                      />
                      <Upload className="w-6 h-6 mx-auto mb-2 text-slate-400" />
                      <p className="text-center text-slate-300 text-sm">
                        {csvFile ? csvFile.name : 'Click to upload CSV'}
                      </p>
                    </label>
                  </div>
                )}

                {/* Predict Button */}
                <button
                  onClick={handlePredict}
                  disabled={loading}
                  className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-slate-600 text-white font-bold py-3 rounded-lg transition duration-200"
                >
                  {loading ? 'Analyzing...' : 'Run Prediction'}
                </button>
              </div>
            </div>
          </div>

          {/* Results Panel */}
          <div className="lg:col-span-2 space-y-6">
            {/* Error Display */}
            {error && (
              <div className="bg-red-900/30 border border-red-600 rounded-lg p-4 flex gap-3">
                <AlertCircle className="w-5 h-5 text-red-400 flex-shrink-0 mt-0.5" />
                <p className="text-red-200">{error}</p>
              </div>
            )}

            {/* Preview Section */}
            {(imagePreview || csvPreview) && (
              <div className="bg-slate-800 rounded-lg border border-slate-700 p-6">
                <h3 className="text-lg font-bold text-white mb-4">Upload Preview</h3>
                <div className="grid grid-cols-2 gap-4">
                  {imagePreview && (
                    <div>
                      <p className="text-sm text-slate-400 mb-2">Image Preview</p>
                      <img src={imagePreview} alt="preview" className="w-full h-40 object-cover rounded border border-slate-600" />
                    </div>
                  )}
                  {csvPreview && (
                    <div>
                      <p className="text-sm text-slate-400 mb-2">CSV Preview</p>
                      <pre className="text-xs text-slate-300 bg-slate-900 p-3 rounded border border-slate-600 overflow-auto h-40">
                        {csvPreview}
                      </pre>
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* Results Display */}
            {results && (
              <div className="space-y-4">
                {/* Overall Risk Score */}
                <div className={`rounded-lg border-2 p-6 ${getRiskColor(results.final_risk_score)}`}>
                  <h3 className={`text-2xl font-bold ${getRiskTextColor(results.final_risk_score)} mb-2`}>
                    {getRiskLabel(results.final_risk_score)}
                  </h3>
                  <div className="flex items-center gap-2">
                    {results.final_risk_score < 0.67 ? (
                      <CheckCircle className="w-5 h-5 text-green-600" />
                    ) : (
                      <AlertCircle className="w-5 h-5 text-red-600" />
                    )}
                    <p className="text-sm font-semibold">
                      Final Risk Score: <span className="text-lg">{(results.final_risk_score * 100).toFixed(1)}%</span>
                    </p>
                  </div>
                </div>

                {/* Detailed Metrics */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {results.image_defect_prob !== undefined && (
                    <div className="bg-slate-800 border border-slate-700 rounded-lg p-4">
                      <p className="text-slate-400 text-sm mb-2">📷 Visual Defect Probability</p>
                      <p className="text-3xl font-bold text-blue-400">{(results.image_defect_prob * 100).toFixed(1)}%</p>
                      <div className="mt-3 w-full bg-slate-700 rounded-full h-2">
                        <div
                          className="bg-blue-500 h-2 rounded-full transition-all"
                          style={{ width: `${results.image_defect_prob * 100}%` }}
                        ></div>
                      </div>
                    </div>
                  )}
                  {results.sensor_anomaly_score !== undefined && (
                    <div className="bg-slate-800 border border-slate-700 rounded-lg p-4">
                      <p className="text-slate-400 text-sm mb-2">📊 Sensor Anomaly Score</p>
                      <p className="text-3xl font-bold text-purple-400">{(results.sensor_anomaly_score * 100).toFixed(1)}%</p>
                      <div className="mt-3 w-full bg-slate-700 rounded-full h-2">
                        <div
                          className="bg-purple-500 h-2 rounded-full transition-all"
                          style={{ width: `${Math.min(results.sensor_anomaly_score * 100, 100)}%` }}
                        ></div>
                      </div>
                    </div>
                  )}
                </div>

                {/* HITL Status */}
                {results.needs_human_review && (
                  <div className="bg-yellow-900/30 border border-yellow-600 rounded-lg p-4 flex gap-3">
                    <AlertCircle className="w-5 h-5 text-yellow-400 flex-shrink-0 mt-0.5" />
                    <div>
                      <p className="text-yellow-200 font-semibold">Human Review Required</p>
                      <p className="text-yellow-300 text-sm">This sample has uncertain prediction and requires expert review.</p>
                    </div>
                  </div>
                )}

                {/* Explanation Section */}
                {results.explanation && (
                  <div className="bg-slate-800 border border-slate-700 rounded-lg p-4">
                    <p className="text-sm font-semibold text-white mb-3">📋 Sensor Explanation</p>
                    <div className="text-sm text-slate-300 space-y-2">
                      {Object.entries(results.explanation).map(([key, value]) => (
                        <div key={key} className="flex justify-between">
                          <span className="capitalize">{key.replace(/_/g, ' ')}</span>
                          <span className="font-mono text-slate-400">{typeof value === 'number' ? value.toFixed(3) : value}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Processing Time */}
                <div className="bg-slate-800 border border-slate-700 rounded-lg p-4 text-center">
                  <p className="text-sm text-slate-400">Processing Time: <span className="text-slate-200 font-semibold">{results.processing_time_ms}ms</span></p>
                </div>
              </div>
            )}

            {/* Empty State */}
            {!results && !error && (
              <div className="bg-slate-800 rounded-lg border border-slate-700 p-12 text-center">
                <p className="text-slate-400">Upload files and click "Run Prediction" to see results here</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}