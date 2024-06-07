import React from "react";

interface ModalProps {
    onClose: () => void;
  }
  
const Modal: React.FC<ModalProps> = ({ onClose }) => {
    return (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
        <div className="bg-white w-[25vw] p-6 rounded-3xl">
            <h2 className="text-[4rem] mb-4">FAQs</h2>
            <p className="mb-4 text-xl tracking-tight">How does this app work?</p>
            <p className="mb-8 text-xl tracking-tight">Where are these verses sourced from?</p>
            <button onClick={onClose} className="border border-black text-black px-4 py-2 rounded-full">
            Try it out!
            </button>
        </div>
        </div>
    );
    };
  
export default Modal;