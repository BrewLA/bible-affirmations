import { useState, useEffect } from "react";

const useAnimateWords = (text: string) => {
  const [animatedText, setAnimatedText] = useState<string[]>([]);

  useEffect(() => {
    if (!text) return;

    const words = text.split(" ");
    words.forEach((word, index) => {
      setTimeout(() => {
        setAnimatedText((prev) => [...prev, word]);
      }, index * 200); // Adjust the delay time as needed
    });

    return () => setAnimatedText([]); // Reset on text change or unmount
  }, [text]);

  return animatedText;
};

export default useAnimateWords;
