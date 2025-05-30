const axios = require("axios");

exports.getCodeReview = async (req, res) => {
  const { code } = req.body;
  try {
    const response = await axios.post("http://localhost:8000/review", { code });
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: "AI service error" });
  }
};