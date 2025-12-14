import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api";
import { useAuth } from "../auth/useAuth";

export default function Dashboard() {
  const [sweets, setSweets] = useState([]);
  const { logout } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    api.get("/api/sweets").then((res) => {
      setSweets(res.data);
    });
  }, []);

  const buy = async (id) => {
    await api.post(`/api/sweets/${id}/purchase`);
    const res = await api.get("/api/sweets");
    setSweets(res.data);
  };

  const handleLogout = () => {
    logout();
    navigate("/");
  };

  return (
    <div>
      <p
        style={{ cursor: "pointer", textDecoration: "underline" }}
        onClick={handleLogout}
      >
        Logout
      </p>

      <h2>Sweets</h2>

      <ul>
        {sweets.map((s) => (
          <li key={s.id}>
            {s.name} — ₹{s.price} — Stock: {s.quantity}{" "}
            <button
              onClick={() => buy(s.id)}
              disabled={s.quantity === 0}
            >
              Buy
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
