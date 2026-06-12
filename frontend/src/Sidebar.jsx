function Sidebar({
  chats,
  createNewChat,
  loadChat,
  currentChat,
}) {
  return (
    <div className="sidebar">

      <button
        className="new-chat-btn"
        onClick={createNewChat}
      >
        + New Chat
      </button>

      <div className="chat-history">

        {chats.map((chat, index) => (
          <div
            key={index}
            className={
              currentChat === index
                ? "chat-item active"
                : "chat-item"
            }
            onClick={() => loadChat(index)}
          >
            💬 {chat.title}
          </div>
        ))}

      </div>

    </div>
  );
}

export default Sidebar;