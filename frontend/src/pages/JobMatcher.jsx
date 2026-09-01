import { useState } from "react";
import { matchJob } from "../api/api";
import { Target, Loader2, CheckCircle2, XCircle } from "lucide-react";
import ReactMarkdown from 'react-markdown';

export default function JobMatcher() {
  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  const handleMatch = async () => {
    if (!file) {
      setError("Please select a resume first");
      return;
    }
    if (!jobDescription.trim()) {
      setError("Please enter a job description");
      return;
    }
    setError("");
    setLoading(true);
    setResult(null);

    try {
      const data = await matchJob(file, jobDescription);
      if (data.success) {
        setResult(data.result);
      } else {
        setError(data.error || "Failed to match job");
      }
    } catch (err) {
      setError("An error occurred during matching");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-white rounded-2xl shadow-sm border border-gray-200 p-8">
        <h2 className="text-2xl font-bold text-gray-900 mb-6 flex items-center">
          <Target className="w-6 h-6 text-blue-600 mr-2" />
          Job Matcher
        </h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">1. Upload Resume</label>
            <div className="border-2 border-dashed border-gray-300 rounded-xl p-6 flex flex-col items-center justify-center bg-gray-50 hover:bg-gray-100 transition-colors cursor-pointer relative h-48">
              <input 
                type="file" 
                accept=".pdf,.docx,.txt" 
                onChange={handleFileChange}
                className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
              />
              <p className="text-sm font-medium text-gray-900 text-center">
                {file ? file.name : "Click or drag file here"}
              </p>
            </div>
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">2. Paste Job Description</label>
            <textarea
              className="w-full h-48 p-4 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-gray-50"
              placeholder="Paste the job description here..."
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
            />
          </div>
        </div>

        {error && (
          <div className="mt-6 p-4 bg-red-50 text-red-700 rounded-lg flex items-center">
            <XCircle className="w-5 h-5 mr-2" />
            {error}
          </div>
        )}

        <div className="mt-8 flex justify-end">
          <button 
            onClick={handleMatch} 
            disabled={!file || !jobDescription || loading}
            className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-xl shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
          >
            {loading && <Loader2 className="w-5 h-5 mr-2 animate-spin" />}
            {loading ? "Matching..." : "Match Job"}
          </button>
        </div>
      </div>

      {result && (
        <div className="mt-8 bg-white rounded-2xl shadow-sm border border-gray-200 p-8">
          <div className="flex items-center mb-6 border-b border-gray-100 pb-4">
            <CheckCircle2 className="w-6 h-6 text-green-500 mr-2" />
            <h3 className="text-xl font-bold text-gray-900">Match Results</h3>
          </div>
          <div className="prose prose-blue max-w-none">
             <ReactMarkdown>{result}</ReactMarkdown>
          </div>
        </div>
      )}
    </div>
  );
}
