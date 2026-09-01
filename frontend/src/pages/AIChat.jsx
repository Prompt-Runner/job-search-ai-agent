import { useState, useRef, useEffect } from "react";
import { chatWithAssistant } from "../api/api";
import { Send, Bot, User, Loader2, Paperclip } from "lucide-react";
import ReactMarkdown from 'react-markdown';

export default function AIChat() {
  const [messages, setMessages] = useState([
    { role: "assistant", text: "Hello! I am your AI Career Assistant. You can ask me for career advice, interview tips, or upload your resume for tailored insights!" }
  ]);
  const [input, setInput] = useState("");
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim() && !file) return;

    const userMessage = { role: "user", text: input || `(Uploaded resume: ${file.name})` };
    setMessages((prev) => [...prev, userMessage]);
    
    const messageToSend = input;
    const fileToSend = file;
    
    setInput("");
    setFile(null);
    setLoading(true);

    try {
      const data = await chatWithAssistant(messageToSend, fileToSend);
      if (data.success) {
        setMessages((prev) => [...prev, { role: "assistant", text: data.response }]);
      } else {
        setMessages((prev) => [...prev, { role: "assistant", text: "Sorry, I encountered an error. Please try again." }]);
      }
    } catch (err) {
      setMessages((prev) => [...prev, { role: "assistant", text: "Network error occurred." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto h-[80vh] flex flex-col bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
      <div className="bg-purple-600 p-4 flex items-center text-white">
        <Bot className="w-6 h-6 mr-3" />
        <h2 className="text-xl font-bold">Career Assistant</h2>
      </div>

      <div className="flex-1 p-6 overflow-y-auto bg-gray-50 space-y-6">
        {messages.map((msg, idx) => (
          <div key={idx} className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}>
            <div className={`flex max-w-[80%] ${msg.role === "user" ? "flex-row-reverse" : "flex-row"}`}>
              <div className={`flex-shrink-0 h-10 w-10 rounded-full flex items-center justify-center ${msg.role === "user" ? "bg-indigo-100 ml-3" : "bg-purple-100 mr-3"}`}>
                {msg.role === "user" ? <User className="w-6 h-6 text-indigo-600" /> : <Bot className="w-6 h-6 text-purple-600" />}
              </div>
              <div className={`p-4 rounded-2xl ${msg.role === "user" ? "bg-indigo-600 text-white rounded-tr-none" : "bg-white border border-gray-200 text-gray-800 rounded-tl-none shadow-sm"}`}>
                {msg.role === "user" ? (
                  <p>{msg.text}</p>
                ) : (
                  <div className="prose prose-sm max-w-none">
                    <ReactMarkdown>{msg.text}</ReactMarkdown>
                  </div>
                )}
              </div>
            </div>
          </div>
        ))}
        {loading && (
          <div className="flex justify-start">
            <div className="flex max-w-[80%] flex-row">
              <div className="flex-shrink-0 h-10 w-10 rounded-full bg-purple-100 mr-3 flex items-center justify-center">
                <Bot className="w-6 h-6 text-purple-600" />
              </div>
              <div className="p-4 rounded-2xl bg-white border border-gray-200 text-gray-800 rounded-tl-none shadow-sm flex items-center">
                <Loader2 className="w-5 h-5 animate-spin text-purple-600 mr-2" />
                Thinking...
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="p-4 bg-white border-t border-gray-200">
        {file && (
          <div className="mb-2 p-2 bg-purple-50 text-purple-700 text-sm rounded-lg flex items-center justify-between">
            <span>Attached: {file.name}</span>
            <button onClick={() => setFile(null)} className="text-purple-700 hover:text-purple-900 font-bold">X</button>
          </div>
        )}
        <form onSubmit={handleSend} className="flex gap-2">
          <label className="flex-shrink-0 bg-gray-100 p-3 rounded-xl cursor-pointer hover:bg-gray-200 transition-colors flex items-center justify-center">
            <Paperclip className="w-5 h-5 text-gray-600" />
            <input type="file" className="hidden" accept=".pdf,.docx,.txt" onChange={(e) => setFile(e.target.files[0])} />
          </label>
          <input
            type="text"
            className="flex-1 border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-purple-500 bg-gray-50"
            placeholder="Type your message..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
          <button
            type="submit"
            disabled={loading || (!input.trim() && !file)}
            className="flex-shrink-0 bg-purple-600 text-white p-3 rounded-xl hover:bg-purple-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center"
          >
            <Send className="w-5 h-5" />
          </button>
        </form>
      </div>
    </div>
  );
}
