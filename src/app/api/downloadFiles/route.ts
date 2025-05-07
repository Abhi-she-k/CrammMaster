import { NextRequest } from 'next/server';
import multer from 'multer';
import path from "path";
import { writeFile } from "fs/promises";
import { stat, write } from 'fs';

const fs = require('fs');

export async function POST(req: NextRequest){
  // Example response data
  try {
    var files = await req.formData();

    const fileStoragePath = 'tmp/uploads'
    // const directoryContent =  fs.readdirSync(fileStoragePath);

    // console.log(directoryContent)

    // if(directoryContent.length > 0){
            
    //   directoryContent.forEach(async (fileName: string) => {
    //     console.log(path.join(fileStoragePath, fileName))
    //     await fs.rm(path.join(fileStoragePath, fileName), (err: any) =>{
    //       if(err){
    //         return new Response(JSON.stringify({error: "Error removing content in 'tmp/uploads' folder", status: 400 }))
    //       }
    //     });
    //   });
    // }

    if(Array.from(files.keys()).length === 0) {

      return new Response(JSON.stringify({ error: "No files found", status: 400 }));

    }  
  
    files.forEach(async (file) => {
      if (file instanceof File) {
        // Convert the file to an ArrayBuffer
        const pathToFile = path.join(fileStoragePath, file.name);
        const bytes = await file.arrayBuffer();
        const buffer = await Buffer.from(bytes);
        await writeFile(pathToFile, buffer);    
      } else {
        return new Response(JSON.stringify({ error: "No file found or invalid file type.", status: 400 }));
      }
    });

    return new Response(JSON.stringify({ message: "File uploaded successfully", status: 200 }));
  }
  catch{
    return new Response(JSON.stringify({ error: "Could not process files", status : 400}));
  }
}