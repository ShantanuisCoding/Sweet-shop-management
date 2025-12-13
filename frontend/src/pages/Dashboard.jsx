import { useEffect, useState } from "react";
import api from "../api";
import SweetCard from "../components/SweetCard";

export default function Dashboard() {
  const [sweets, setSweets] = useState([]);
  const [error, setError] = useState(null);

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

  return (
    <div>
      <h2>Dashboard</h2>

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
