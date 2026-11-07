const API_URL = "http://127.0.0.1:8000/api";


export const sendMessage = async (question) => {
  try {
    const response = await fetch(`${API_URL}/chat`, {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        question: question,
      }),
    });

    if (!response.ok) {
      const errorData = await response.json();

      throw new Error(
        errorData.detail || "Failed to get AI response."
      );
    }

    const data = await response.json();

    return data;

  } catch (error) {
    console.error("Chat API Error:", error);

    throw error;
  }
};