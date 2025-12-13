import { useEffect, useState } from "react";
import api from "../api";
import SweetCard from "../components/SweetCard";

export default function Dashboard() {
  const [sweets, setSweets] = useState([]);

  useEffect(() => {
    api.get("/api/sweets").then(res => setSweets(res.data));
  }, []);

  return (
    <div>
      <h2>Sweets</h2>
      {sweets.map(s => (
        <SweetCard key={s.id} sweet={s} onUpdate={setSweets} />
      ))}
    </div>
  );
}
