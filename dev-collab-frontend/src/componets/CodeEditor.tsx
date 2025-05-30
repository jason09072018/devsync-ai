// dev-collab-frontend/src/components/CodeEditor.tsx
import { useEffect, useState } from "react";
import Editor from "@monaco-editor/react";
import { io, Socket } from "socket.io-client";

const CodeEditor = ({ roomId }: { roomId: string }) => {
  const [code, setCode] = useState("");
  const [socket, setSocket] = useState<Socket | null>(null);

  useEffect(() => {
    const newSocket = io("http://localhost:5000");
    newSocket.emit("join-room", roomId);
    setSocket(newSocket);

    // Listen for code updates
    newSocket.on("code-update", (newCode: string) => {
      setCode(newCode);
    });

    return () => { newSocket.disconnect(); };
  }, [roomId]);

  const handleEditorChange = (value: string | undefined) => {
    if (value && socket) {
      setCode(value);
      socket.emit("code-change", value, roomId); // Emit changes to room
    }
  };

  return (
    <Editor
      height="90vh"
      defaultLanguage="javascript"
      value={code}
      onChange={handleEditorChange}
    />
  );
};