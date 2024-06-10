import React from "react";
import Accordion from "./Accordion";
import ParticlesBackground from "@/hooks/ParticlesBackground";

interface ModalProps {
    onClose: () => void;
  }
  
const Modal: React.FC<ModalProps> = ({ onClose }) => {
    return (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-65 z-50">
            <div className="bg-white w-[25vw] p-6 rounded-3xl flex flex-col">
                <h2 className="text-[4rem] text-black mb-4">FAQs</h2>
                <div className="container mx-auto">
                    <Accordion title="How does it work?" content="This app is powered by the DistilBERT AI model, which uses sentiment analysis to determine whether your response holds Positive or Negative connotation. From there, it will output a Bible verse as an affirmation!" />
                    <Accordion title="Is it free to use?" content="Although we plan on scaling this web app, it is currently free, so please use it as much as you'd like!" />
                    <Accordion title="Are my responses saved?" content="We currently have it set where only you can see your responses, and other users will not be able to view your responses. Our goal is to eventually build a community thread for users to openly share their stories and verses that they were given." />
                </div>
                <button onClick={onClose} className="flex relative w-full bg-[#BC896C] text-white py-3 justify-center items-center rounded-xl overflow-hidden">
                    Try it out!
                    <div className="absolute z-0">
                        <ParticlesBackground />
                    </div>
                </button>
            </div>
        </div>
    );
    };
  
export default Modal;