export default {
  api: "http://localhost:8000",
  BEARER_AUTH: `Bearer ${localStorage.getItem("token")}`,
};
