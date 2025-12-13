import { createContext, useState } from "react";
import { setAuthToken } from "../api";

export const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [token, setToken] = useState(
    localStorage.getItem("token")
  );

  const login = (jwt) => {
    localStorage.setItem("token", jwt);
    setAuthToken(jwt);
    setToken(jwt);
  };

  const logout = () => {
    localStorage.removeItem("token");
    setAuthToken(null);
    setToken(null);
  };

  return (
    <AuthContext.Provider value={{ token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
