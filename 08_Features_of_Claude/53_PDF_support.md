# 53. PDF support

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287768
**Section:** 08 Features of Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    1
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    PDF support
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Claude can read and analyze PDF files directly, making it a powerful tool for document processing. This capability works similarly to image processing, but with a few key differences in how you structure your code.

Setting Up PDF Processing

To process a PDF file with Claude, you'll use nearly identical code to what you'd use for images. The main differences are in the file type specifications and variable names for clarity.

Here's how to modify your existing image processing code for PDFs:

with open("earth.pdf", "rb") as f:
    file_bytes = base64.standard_b64encode(f.read()).decode("utf-8")

messages = []

add_user_message(
    messages,
    [
        {
            "type": "document",
            "source": {
                "type": "base64",
                "media_type": "application/pdf",
                "data": file_bytes,
            },
        },
        {"type": "text", "text": "Summarize the document in one sentence"},
    ],
)

chat(messages)

Key Changes from Image Processing

When adapting your image processing code for PDFs, you need to update several elements:

Change the file extension from .png to .pdf
Update the variable name from image_bytes to file_bytes for clarity
Set the type to "document" instead of "image"
Change the media type to "application/pdf" instead of "image/png"

What Claude Can Extract from PDFs

Claude's PDF processing capabilities go beyond simple text extraction. It can analyze and understand:

Text content throughout the document
Images and charts embedded in the PDF
Tables and their data relationships
Document structure and formatting

This makes Claude essentially a one-stop solution for extracting any type of information from PDF documents, whether you need summaries, data analysis, or specific content extraction.

The example above shows Claude successfully processing a Wikipedia article about Earth that was saved as a PDF, demonstrating how it can understand and summarize complex document content in a single sentence.
                            
                        
                    

                    
                        
                            Downloads
                            
                                
                                    
                                        
                                            
                                            
                                                earth.pdf
                                                (opens in new tab)

---

## 🎬 Transcript (English)

Besides images, Claude can also read content directly out of a PDF file. I'm going to show you how you do that in this video. Attached to this video, you will find a document called earth.pdf. If you open it up, you'll see that it's just a couple of pages out of the Wikipedia article on Earth. So make sure you download this PDF file and place it inside the same directory as your notebook. To read a PDF file, we use almost the exact same code that we use for reading an image and feeding the image into Claude. So I'm going to find where we are currently opening up an image right here, and I'm going to change it to earth.pdf. I'm going to rename this variable from image bytes to how about file bytes, because no longer are we reading an image. I'm going to make sure I update the variable down here as well. I'm going to change the type right here from image to document, and then the media type will go from image slash png to application slash pdf. And then finally, the question that we're asking of Claude about this document, rather than feeding in our big prompt that we have in the previous cell, I'm going to ask Claude to summarize the document in one sentence. And let's see what we get out of Claude. So I'm going to run this. And there's the summary. It looks like it successfully read the contents of that PDF file. Now, Claude has the ability to not only read text out of a PDF, it can also read images or charts, tables, and so on. So you should really think of Claude as being like a one stop shop for extracting just about any kind of information out of a PDF document.

---

## 🎬 トランスクリプト（日本語）

画像以外にも、Claudeはコンテンツを読み取ることができます PDFファイルから直接。このビデオでその方法を説明します このビデオに添付されているドキュメント earth.pdf という名前のファイルがあります。 開くと、これは数ページしかないことがわかります。 Wikipedia の地球に関する記事からです。ですから、 この PDF ファイルをダウンロードして、同じ場所に配置してください。 ディレクトリにノートブックを置きます。PDF を読み取るには 画像を読むときに使うコードとほぼ同じコードを使用します。 画像を Claude に入力します。ですから 現在画像を開いている場所を見つけます。 そして、それを earth.pdf に変更します。 この変数を image bytes から file bytes に変更します。もう画像は読んでいないからです。 下に変数も更新します。 このタイプのところを変更します。 画像からドキュメントに変更します。 そして、メディアタイプは画像スラッシュから png から application slash pdf になります。 そして最後に、Claude に尋ねている質問は このドキュメントについて、前のセルにある大きなプロンプトを フィードするのではなく、Claude に ドキュメントを1文で要約するように依頼します。 そして Claude から何が得られるか見てみましょう。なので これを実行します。そして その要約です。PDF ファイルの内容を正常に読み取ったようです。 Claude は PDF からテキストを読み取るだけでなく 画像やチャート、テーブルなども読み取ることができます。 だから Claude を、ほぼすべての種類の情報を抽出するための ワンストップショップとして考えるべきです。 PDF ドキュメントから。
