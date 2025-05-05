import Head from "next/head";
'use client';
import FileUpload from '@/app/components/FileUpload';
import LearnButton from '@/app/components/LearnButton';


import { useState} from 'react';


export default function Home() {
  const [filesUploaded, setFilesUploaded] = useState<File[]>([]);
  return (
    <div className="flex flex-col items-center text-center">
      <FileUpload filesUploaded={filesUploaded} setFilesUploaded={setFilesUploaded} />
      <LearnButton filesUploaded={filesUploaded} setFilesUploaded={setFilesUploaded} />
    </div>

  );
}
