import { useState } from "react";
import { Button } from "@/components/ui/button";

export default function Calculator() {
  const [display, setDisplay] = useState("0");
  const [expression, setExpression] = useState("");

  const handleClick = (value) => {
    if (value === "C") {
      setDisplay("0");
      setExpression("");
    } else if (value === "=") {
      fetch("http://localhost:5000/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ expression }),
      })
        .then((res) => res.json())
        .then((data) => setDisplay(data.result))
        .catch(() => setDisplay("Error"));
    } else {
      setExpression((prev) => prev + value);
      setDisplay((prev) => (prev === "0" ? value : prev + value));
    }
  };

  const buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
  ];

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <div className="bg-white p-6 rounded-lg shadow-lg w-64">
        <div className="bg-gray-200 text-right p-3 mb-3 text-xl font-mono rounded">{display}</div>
        <div className="grid grid-cols-4 gap-2">
          {buttons.map((btn) => (
            <Button key={btn} className="p-4 text-xl" onClick={() => handleClick(btn)}>
              {btn}
            </Button>
          ))}
        </div>
      </div>
    </div>
  );
}
