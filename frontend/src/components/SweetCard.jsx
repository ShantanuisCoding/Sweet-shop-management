export default function SweetCard({ sweet, onPurchase }) {
  return (
    <li>
      <strong>{sweet.name}</strong> | {sweet.category} | ₹{sweet.price} | Stock: {sweet.quantity}{" "}
      <button
        onClick={() => onPurchase(sweet.id)}
        disabled={sweet.quantity === 0}
      >
        Purchase
      </button>
    </li>
  );
}
