import api from "../api";

export default function SweetCard({ sweet, onUpdate }) {
  const purchase = async () => {
    await api.post(`/api/sweets/${sweet.id}/purchase`);
    const res = await api.get("/api/sweets");
    onUpdate(res.data);
  };

  return (
    <div style={{ border: "1px solid #ccc", margin: 8, padding: 8 }}>
      <h4>{sweet.name}</h4>
      <p>Category: {sweet.category}</p>
      <p>Price: ₹{sweet.price}</p>
      <p>Stock: {sweet.quantity}</p>

      <button disabled={sweet.quantity === 0} onClick={purchase}>
        Purchase
      </button>
    </div>
  );
}
