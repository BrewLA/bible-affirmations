import React from "react";
import Accordion from "./Accordion";

interface ModalProps {
    onClose: () => void;
  }
  
const Modal: React.FC<ModalProps> = ({ onClose }) => {
    return (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
        <div className="bg-white w-[25vw] p-6 rounded-3xl flex flex-col">
            <h2 className="text-[4rem] mb-4">FAQs</h2>
            <div className="container mx-auto">
                <Accordion title="How does it work?" content="This app is powered by the DistilBERT AI model, which uses sentiment analysis to determine whether your response holds Positive or Negative connotation. From there, it will output a Bible verse as an affirmation!" />
                <Accordion title="Is it free to use?" content="Although we plan on scaling this web app, it is currently free, so please use it as much as you'd like!" />
                <Accordion title="Are my responses saved?" content="We currently have access to user input on our backend, but other users will not be able to see your responses. Our goal is to eventually build a community thread for users to openly share their stories and verses that they were given." />
            </div>
            <button onClick={onClose} className="border border-black hover:bg-black hover:text-white text-black px-4 py-2 rounded-xl">
            Try it out!
            </button>
        </div>
        </div>
    );
    };
  
export default Modal;