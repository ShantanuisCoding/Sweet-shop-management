import { useEffect, useState } from "react";
import api from "../api";

export default function Dashboard() {
  const [sweets, setSweets] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    api
      .get("/api/sweets")
      .then((res) => setSweets(res.data))
      .catch(() => setError("Failed to load sweets"));
  }, []);

  return (
    <div>
      <h2>Dashboard</h2>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <ul>
        {sweets.map((sweet) => (
          <li key={sweet.id}>
            <strong>{sweet.name}</strong> | {sweet.category} | ₹{sweet.price} | Stock: {sweet.quantity}
          </li>
        ))}
      </ul>
    </div>
  );
}
