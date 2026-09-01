import { useState } from "react";
import { analyzeResume } from "../api/api";
import { FileUp, Loader2, CheckCircle2, XCircle } from "lucide-react";
import ReactMarkdown from 'react-markdown';

export default function AnalyzeResume() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a file first");
      return;
    }
    setError("");
    setLoading(true);
    setResult(null);

    try {
      const data = await analyzeResume(file);
      if (data.success) {
        // Assume data.analysis is a markdown string from Gemini
        setResult(data.analysis);
      } else {
        setError(data.error || "Failed to analyze resume");
      }
    } catch (err) {
      setError("An error occurred during analysis");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-white rounded-2xl shadow-sm border border-gray-200 p-8">
        <h2 className="text-2xl font-bold text-gray-900 mb-6">Analyze Your Resume</h2>
        
        <div className="border-2 border-dashed border-gray-300 rounded-xl p-10 flex flex-col items-center justify-center bg-gray-50 hover:bg-gray-100 transition-colors cursor-pointer relative">
          <input 
            type="file" 
            accept=".pdf,.docx,.txt" 
            onChange={handleFileChange}
            className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
          />
          <FileUp className="w-12 h-12 text-indigo-400 mb-4" />
          <p className="text-lg font-medium text-gray-900">
            {file ? file.name : "Drag and drop your resume or click to browse"}
          </p>
          <p className="text-sm text-gray-500 mt-2">Supports PDF, DOCX, and TXT</p>
        </div>

        {error && (
          <div className="mt-4 p-4 bg-red-50 text-red-700 rounded-lg flex items-center">
            <XCircle className="w-5 h-5 mr-2" />
            {error}
          </div>
        )}

        <div className="mt-6 flex justify-end">
          <button 
            onClick={handleUpload} 
            disabled={!file || loading}
            className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-xl shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
          >
            {loading && <Loader2 className="w-5 h-5 mr-2 animate-spin" />}
            {loading ? "Analyzing..." : "Analyze Resume"}
          </button>
        </div>
      </div>

      {result && (
        <div className="mt-8 bg-white rounded-2xl shadow-sm border border-gray-200 p-8">
          <div className="flex items-center mb-6 border-b border-gray-100 pb-4">
            <CheckCircle2 className="w-6 h-6 text-green-500 mr-2" />
            <h3 className="text-xl font-bold text-gray-900">Analysis Results</h3>
          </div>
          <div className="prose prose-indigo max-w-none">
             <ReactMarkdown>{result}</ReactMarkdown>
          </div>
        </div>
      )}
    </div>
  );
}
