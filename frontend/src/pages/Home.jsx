import { Link } from "react-router-dom";
import { ArrowRight, FileText, Upload, MessageSquare } from "lucide-react";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-3xl text-center">
        <h1 className="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl md:text-6xl">
          <span className="block xl:inline">Supercharge Your </span>
          <span className="block text-indigo-600 xl:inline">Job Search</span>
        </h1>
        <p className="mt-3 max-w-md mx-auto text-base text-gray-500 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl">
          Use the power of AI to analyze your resume, find the perfect job matches, and get career advice tailored just for you.
        </p>
      </div>
      
      <div className="mt-16 grid gap-8 md:grid-cols-3 max-w-5xl mx-auto">
        {/* Feature 1 */}
        <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-8 hover:shadow-md transition-shadow">
          <div className="w-12 h-12 bg-indigo-100 rounded-xl flex items-center justify-center mb-6">
            <FileText className="w-6 h-6 text-indigo-600" />
          </div>
          <h3 className="text-xl font-bold text-gray-900 mb-2">Resume Analysis</h3>
          <p className="text-gray-500 mb-6">Get an ATS score, discover your strengths, and find areas for improvement.</p>
          <Link to="/analyze" className="text-indigo-600 font-medium inline-flex items-center hover:text-indigo-700">
            Analyze Now <ArrowRight className="ml-2 w-4 h-4" />
          </Link>
        </div>

        {/* Feature 2 */}
        <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-8 hover:shadow-md transition-shadow">
          <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center mb-6">
            <Upload className="w-6 h-6 text-blue-600" />
          </div>
          <h3 className="text-xl font-bold text-gray-900 mb-2">Job Matcher</h3>
          <p className="text-gray-500 mb-6">Compare your resume against a job description to see if you are a good fit.</p>
          <Link to="/match" className="text-blue-600 font-medium inline-flex items-center hover:text-blue-700">
            Find Matches <ArrowRight className="ml-2 w-4 h-4" />
          </Link>
        </div>

        {/* Feature 3 */}
        <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-8 hover:shadow-md transition-shadow">
          <div className="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center mb-6">
            <MessageSquare className="w-6 h-6 text-purple-600" />
          </div>
          <h3 className="text-xl font-bold text-gray-900 mb-2">AI Assistant</h3>
          <p className="text-gray-500 mb-6">Chat with our career assistant about interview tips and career growth.</p>
          <Link to="/chat" className="text-purple-600 font-medium inline-flex items-center hover:text-purple-700">
            Start Chat <ArrowRight className="ml-2 w-4 h-4" />
          </Link>
        </div>
      </div>
    </div>
  );
}
