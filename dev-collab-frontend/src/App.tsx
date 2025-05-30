import React, { useEffect, useState } from "react";
import "./index.css";


type User = {
  id: number;
  login: string;
  avatar_url: string;
};

function App() {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    fetch("http://localhost:5000/api/me", {
      credentials: "include",
    })
      .then(async (res) => {
        if (!res.ok) return setUser(null);
        const data = await res.json();
        setUser(data);
      })
      .catch(() => setUser(null));
  }, []);

  const handleLogin = () => {
    const clientId = import.meta.env.VITE_GITHUB_CLIENT_ID;
    const redirectUri = "http://localhost:5000/api/auth/github/callback";
    const githubAuthUrl = `https://github.com/login/oauth/authorize?client_id=${clientId}&redirect_uri=${redirectUri}`;
    window.location.href = githubAuthUrl;
  };

  const handleLogout = () => {
    fetch("http://localhost:5000/api/logout", {
      credentials: "include",
    }).then(() => {
      setUser(null);
      window.location.reload();
    });
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-100 to-gray-300 flex items-center justify-center px-4">
      <div className="bg-white shadow-2xl rounded-2xl p-8 max-w-sm w-full text-center">
        <h1 className="text-3xl font-bold mb-6 text-gray-800">DevSync AI</h1>

        {user ? (
          <>
            <img
              src={user.avatar_url}
              alt="avatar"
              className="w-24 h-24 mx-auto rounded-full mb-4 border-4 border-gray-300"
            />
            <h2 className="text-xl font-semibold text-gray-700 mb-2">{user.login}</h2>
            <button
              onClick={handleLogout}
              className="mt-4 px-4 py-2 bg-red-500 text-white rounded-full hover:bg-red-600 transition"
            >
              Logout
            </button>

            <div className="mt-8 text-left">
              <h3 className="text-lg font-semibold text-gray-700 mb-2">🎯 Dashboard</h3>
              <p className="text-gray-600">Welcome to your authenticated area!</p>
            </div>
          </>
        ) : (
          <button
            onClick={handleLogin}
            className="px-6 py-3 bg-black text-white rounded-full hover:opacity-90 transition font-semibold"
          >
            Login with GitHub
          </button>
        )}
      </div>
    </div>
  );
}

export default App;
