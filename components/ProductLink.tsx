import Link from 'next/link';
import React from 'react';
import Image from 'next/image';

function ProductLink() {
  return (
    <Link
      href="https://amzn.to/3RkW8dD"
      target="_blank"
      className="flex flex-col w-64 h-auto rounded-xl overflow-hidden"
    >
      <Image
        src="/images/cross-necklace.jpg"
        alt="cross necklace"
        width={384} // Width in pixels
        height={240} // Height in pixels
        className="object-cover"
      />
      <h2 className="font-sans p-4 bg-white">14K Gold Cross Necklace Womens</h2>
    </Link>
  );
}

export default ProductLink;
