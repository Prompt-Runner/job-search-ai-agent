import { Link } from "react-router-dom";
import { Briefcase, FileText, MessageSquare, Upload } from "lucide-react";

export default function Navbar() {
  return (
    <nav className="bg-white shadow-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex">
            <div className="flex-shrink-0 flex items-center">
              <Link to="/" className="text-xl font-bold text-indigo-600 flex items-center gap-2">
                <Briefcase className="w-6 h-6" />
                Job AI Agent
              </Link>
            </div>
            <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
              <Link to="/analyze" className="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">
                <FileText className="w-4 h-4 mr-2" />
                Analyze Resume
              </Link>
              <Link to="/match" className="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">
                <Upload className="w-4 h-4 mr-2" />
                Job Matcher
              </Link>
              <Link to="/chat" className="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">
                <MessageSquare className="w-4 h-4 mr-2" />
                AI Chat
              </Link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
}
