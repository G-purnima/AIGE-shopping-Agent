import { useState } from "react";

function SearchForm({ onSearch, loading }) {
  const [product, setProduct] = useState("");
  const [budget, setBudget] = useState("");
  const [preferences, setPreferences] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    const preferenceList = preferences
      .split(",")
      .map((item) => item.trim())
      .filter((item) => item !== "");

    onSearch({
      product,
      budget: Number(budget),
      preferences: preferenceList,
    });
  };

  return (
    <form onSubmit={handleSubmit} className="search-form">

      <label>What are you looking for?</label>

      <input
        type="text"
        placeholder="e.g. Gaming Laptop"
        value={product}
        onChange={(e) => setProduct(e.target.value)}
        required
      />

      <label>Your Budget</label>

      <input
        type="number"
        placeholder="e.g. 80000"
        value={budget}
        onChange={(e) => setBudget(e.target.value)}
        required
      />

      <label>Preferences</label>

      <input
        type="text"
        placeholder="e.g. 16GB RAM, RTX 4050, Good Battery"
        value={preferences}
        onChange={(e) => setPreferences(e.target.value)}
      />

      <button type="submit" disabled={loading}>
        {loading
          ? "Finding the best product..."
          : "🔍 Find Best Product"}
      </button>

    </form>
  );
}

export default SearchForm;