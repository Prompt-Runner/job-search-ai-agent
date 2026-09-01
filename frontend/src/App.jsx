import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import AnalyzeResume from "./pages/AnalyzeResume";
import JobMatcher from "./pages/JobMatcher";
import AIChat from "./pages/AIChat";

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/analyze" element={<AnalyzeResume />} />
          <Route path="/match" element={<JobMatcher />} />
          <Route path="/chat" element={<AIChat />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
