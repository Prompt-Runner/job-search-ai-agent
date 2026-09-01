import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const uploadResume = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  const response = await axios.post(`${API_URL}/upload-resume`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return response.data;
};

export const analyzeResume = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  const response = await axios.post(`${API_URL}/analyze-resume`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return response.data;
};

export const matchJob = async (file, jobDescription) => {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("job_description", jobDescription);
  const response = await axios.post(`${API_URL}/match-job`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return response.data;
};

export const chatWithAssistant = async (message, file = null) => {
  const formData = new FormData();
  formData.append("message", message);
  if (file) {
    formData.append("file", file);
  }
  const response = await axios.post(`${API_URL}/chat`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return response.data;
};
