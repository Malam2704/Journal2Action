'use client' // 👈 use it here

import { useState } from "react";

export default function Home() {
  const [journal, setJournal] = useState("");

  return (
    <div className="max-w-xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Journal2Action</h1>
      <textarea
        className="w-full h-40 p-2 border rounded"
        value={journal}
        onChange={(e) => setJournal(e.target.value)}
        placeholder="What's on your mind today?"
      />
      <button
        className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
        onClick={() => console.log("Submitted:", journal)}
      >
        Submit
      </button>
      <div className="mt-6 text-gray-500">
        {/* Placeholder for extracted tasks */}
        Your action items will appear here...
      </div>
    </div>
  );
}
