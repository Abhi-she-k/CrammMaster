import { NextRequest } from 'next/server';
import multer from 'multer';
import path from "path";
import { writeFile } from "fs/promises";
import { write } from 'fs';

export async function POST(req: NextRequest) {
  // Example response data
  var files = await req.formData();
  console.log(files);


  files.forEach(async (file) => {
    if (file instanceof File) {
      // Convert the file to an ArrayBuffer
      const bytes = await file.arrayBuffer();
      const buffer = Buffer.from(bytes);
  
      const pathToFile = path.join('/Users/abhishek/Desktop/Projects/crammaster.ai/tmp/uploads', file.name);
      await writeFile(pathToFile, buffer);
  
      console.log("File saved to:", pathToFile);
  
    } else {
      console.error("No file found or invalid file type.");
    }
  });

}