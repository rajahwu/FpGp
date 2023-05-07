import { io } from "socket.io-client";
import { useState, useEffect } from "react";

let socket;

function Message() {
  const [msg, setMsg] = useState("");
  const [chatInput, updateChatInput] = useState("");

  useEffect(() => {
    socket = io();
    socket.on("ping", (chat) => {
    console.log(chat)
      console.log(msg);
    });
    return () => {
      socket.disconnect();
    };
  }, []);

  const sendChat = (e) => {
    e.preventDefault();
    setMsg(chatInput);
    socket.emit("chat", msg);
  };

  return (
    <>
      <h1>Messages</h1>
      <form onSubmit={sendChat}>
        <input value={chatInput} onChange={updateChatInput} />
        <button type="submit">Send</button>
      </form>
    </>
  );
}

export default Message;
