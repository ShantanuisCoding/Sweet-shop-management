import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api";
import SweetCard from "../components/SweetCard";
import { useAuth } from "../auth/useAuth";

export default function Dashboard() {
  const [sweets, setSweets] = useState([]);
  const [error, setError] = useState(null);

  const { logout } = useAuth();
  const navigate = useNavigate();

  const loadSweets = () => {
    api
      .get("/api/sweets")
      .then((res) => setSweets(res.data))
      .catch(() => setError("Failed to load sweets"));
  };

  useEffect(() => {
    loadSweets();
  }, []);

  const purchaseSweet = async (id) => {
    try {
      await api.post(`/api/sweets/${id}/purchase`);
      loadSweets();
    } catch {
      setError("Purchase failed");
    }
  };

  const handleLogout = () => {
    logout();
    navigate("/");
  };

  return (
    <div>
      <h2>Dashboard</h2>

      <button onClick={handleLogout}>Logout</button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <ul>
        {sweets.map((sweet) => (
          <SweetCard
            key={sweet.id}
            sweet={sweet}
            onPurchase={purchaseSweet}
          />
        ))}
      </ul>
    </div>
  );
}
