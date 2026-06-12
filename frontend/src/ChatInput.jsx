import React from "react";

function ChatInput({
  question,
  setQuestion,
  askQuestion,
}) {

  const handlePdfUpload = async (event) => {

    const file = event.target.files[0];

    if (!file) return;

    const formData = new FormData();

    formData.append("file", file);

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/upload-pdf",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      alert(
        `PDF Uploaded!\nCharacters: ${data.characters}`
      );

    } catch (error) {

      console.error(error);

      alert("PDF upload failed.");

    }
  };

  return (
    <div className="input-area">

      {/* PDF Upload */}
      <label className="upload-btn">
        📄
        <input
          type="file"
          accept=".pdf"
          hidden
          onChange={handlePdfUpload}
        />
      </label>

      {/* Text Input */}
      <input
        type="text"
        value={question}
        placeholder="Message AI..."
        onChange={(e) =>
          setQuestion(e.target.value)
        }
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            askQuestion();
          }
        }}
      />

      {/* Mic */}
      <button className="mic-btn">
        🎤
      </button>

      {/* Send */}
      <button
        className="send-btn"
        onClick={askQuestion}
      >
        Send
      </button>

    </div>
  );
}

export default ChatInput;