import { useState } from "react";

import SearchForm from "./components/SearchForm";
import ProductCard from "./components/ProductCard";
import Recommendation from "./components/Recommendation";

import "./App.css";

function App() {

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSearch = async (searchData) => {

    setLoading(true);
    setError("");
    setResult(null);

    try {

      const response = await fetch(
        "https://aige-shopping.onrender.com/recommend",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify(searchData),
        }
      );

      if (!response.ok) {
        throw new Error("Failed to get recommendation");
      }

      const data = await response.json();

      setResult(data);

    } catch (error) {

      console.error(error);

      setError(
        "Something went wrong. Make sure the FastAPI server is running."
      );

    } finally {

      setLoading(false);

    }
  };

  return (

    <div className="app">

      <header>
        <h1>🛍 AI Shopping Agent</h1>

        <p>
          Find the best product based on your budget and preferences.
        </p>
      </header>

      <SearchForm
        onSearch={handleSearch}
        loading={loading}
      />

      {error && (
        <p className="error">
          {error}
        </p>
      )}

      {result && (

        <div className="results">

          <Recommendation
            recommendation={result.recommendation}
          />

          <h2>Products Found</h2>

          <div className="products">

            {result.products.map((product, index) => (

              <ProductCard
                key={index}
                product={product}
              />

            ))}

          </div>

        </div>

      )}

    </div>
  );
}

export default App;