import LinearCircle from "@/components/LinearCircle";
import Modal from "@/components/Modal";
import Link from "next/link";
import { useState } from "react";
import useAnimateWords from "../hooks/useAnimateWords";
import React from "react";

function Index() {
  const [message, setMessage] = useState("");
  const [feeling, setFeeling] = useState("");
  const [error, setError] = useState("");
  const [verse, setVerse] = useState("");
  const [responseMessage, setResponseMessage] = useState("");
  const animatedMessage = useAnimateWords(verse);

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError(""); // Clear previous errors
    
    if (!feeling.trim()) {
      setError("Please describe what's on your mind to receive an affirmation!");
      return;
    }
    
    fetch("https://rashtrq-bible-affirmations.hf.space/api/home", { // Update with your Hugging Face Spaces URL
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ feeling })
    })
      .then(response => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then(data => {
        setVerse(data.verse); // Display Bible verse
        setResponseMessage(data.response_message); // Display sentiment-related message
      })
      .catch(error => {
        console.error("Error fetching data:", error);
        setError("Error fetching data");
      });
  };

  // Modal Interaction
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleOpenModal = () => {
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
  };

  return (
    <main className="flex flex-col gap-8 justify-start items-center">
      <h1 className="text-[15rem] text-secondary">Affirmations</h1>
      <form onSubmit={handleSubmit} className="flex justify-center items-center relative">
        <input
          type="text"
          value={feeling}
          onChange={(e) => setFeeling(e.target.value)}
          placeholder="What's on your mind?"
          className="min-w-[40rem] px-4 py-4 placeholder:text-gray-500 bg-white rounded-full pr-14 focus:outline-none"
        />
        <button type="submit" className="absolute w-[1.5rem] h-[1.5rem] right-4">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><g data-name="92-Arrow Right"><path d="M16 32a16 16 0 1 1 16-16 16 16 0 0 1-16 16zm0-30a14 14 0 1 0 14 14A14 14 0 0 0 16 2z"/><path d="M13.71 24.71 12.3 23.3l7.29-7.3-7.3-7.29L13.7 7.3l8 8a1 1 0 0 1 0 1.41z"/></g></svg>
        </button>
      </form>
      {error && (
        <div className="text-red-500 bg-white p-4 rounded-2xl">
          {error}
        </div>
      )}
      {verse && (
        <div className="max-w-[64rem] border border-white p-12 rounded-[4rem] relative z-50">
          <h2 className="text-center text-primary text-[4rem] leading-[3.8rem]">
            {animatedMessage.map((word, index) => (
              <span
                key={index}
                className="word"
                style={{ animationDelay: `${index * 0}s` }} /* Adjust delay time */
              >
                {word}
              </span>
            ))}
          </h2>
          {responseMessage && (
            <p className="text-center text-primary text-lg mt-8">{responseMessage}</p>
          )}
        </div>
      )}
      <ul className="flex flex-row gap-2 p-4 text-primary relative z-10">
        <li>
          <Link href="#" onClick={handleOpenModal}>FAQs</Link>
        </li>
        |
        <li>
          <Link href="/about">Join our community!</Link>
        </li>
        |
        <li>
          <Link href="/blog/hello-world">View products</Link>
        </li>
        |
        <li>
          <Link
            href="https://brewla.design"
            target="_blank"
            className="text-center text-primary hover:text-white text-base leading-normal">
            Made with ❤️ by the Brew.LA team
          </Link>
        </li>
      </ul>
      <div className="flex flex-row w-full absolute bottom-0 z-0">
        <div className="flex flex-row gap-2 absolute left-[-12rem] bottom-[-2rem] z-0">
          <LinearCircle />
        </div>
        <div className="flex flex-row gap-2 absolute left-[2rem] bottom-[-18rem] z-0">
          <LinearCircle />
        </div>
        <div className="flex flex-row gap-2 absolute right-[-12rem] bottom-[-2rem] rotate-180 z-0">
          <LinearCircle />
        </div>
        <div className="flex flex-row gap-2 absolute right-[2rem] bottom-[-18rem] rotate-180 z-0">
          <LinearCircle />
        </div>
      </div>

      {isModalOpen && <Modal onClose={handleCloseModal} />}
    </main>
  );
}

export default Index;
