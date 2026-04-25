# 54. Citations

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287771
**Section:** 08 Features of Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    2
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Citations
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When Claude answers questions based on documents you provide, users might assume it's just drawing from its training data. But what if Claude could show exactly where it found specific information? That's where citations come in - a powerful feature that lets Claude reference specific parts of your source documents and show users exactly where each piece of information comes from.

Why Citations Matter

Imagine asking Claude about how Earth's atmosphere formed and getting a detailed answer. Without citations, users have no way to verify the information or understand that Claude is actually referencing a specific document you provided. Citations solve this transparency problem by creating a clear trail from Claude's response back to your source material.

Enabling Citations

To enable citations, you need to modify your document message structure. Add two new fields to your document block:

{
    "type": "document",
    "source": {
        "type": "base64",
        "media_type": "application/pdf",
        "data": file_bytes,
    },
    "title": "earth.pdf",
    "citations": { "enabled": True }
}

The title field gives your document a readable name, while citations: {"enabled": True} tells Claude to track where it finds information.

Understanding Citation Structure

When citations are enabled, Claude's response becomes more complex. Instead of simple text, you get structured data that includes citation information for each claim.

Each citation contains several key pieces of information:

cited_text - The exact text from your document that supports Claude's statement
document_index - Which document Claude is referencing (useful when you provide multiple documents)
document_title - The title you assigned to the document
start_page_number - Where the cited text begins
end_page_number - Where the cited text ends

Building User Interfaces with Citations

The real power of citations comes from building user interfaces that make this information accessible. You can create interactive elements where users can hover over citation markers to see exactly where information came from.

This creates a transparent experience where users can:

See that Claude's answers are grounded in actual source material
Verify the information by checking the original document
Understand the context around each cited piece of information

Citations with Plain Text

Citations aren't limited to PDF documents. You can also use them with plain text sources. When working with text, modify your document structure like this:

{
    "type": "document", 
    "source": {
        "type": "text",
        "media_type": "text/plain",
        "data": article_text,
    },
    "title": "earth_article",
    "citations": { "enabled": True }
}

With plain text sources, instead of page numbers, you'll get character positions that pinpoint exactly where in the text Claude found each piece of information.

When to Use Citations

Citations are particularly valuable when:

Users need to verify information for accuracy
You're working with authoritative documents that users should be able to reference
Transparency about information sources is critical for your application
Users might want to explore the broader context around specific facts

By implementing citations, you transform Claude from a "black box" that provides answers into a transparent research assistant that shows its work. This builds user trust and enables them to dive deeper into your source materials when needed.
                            
                        
                    

                    
                        
                            Downloads
                            
                                
                                    
                                        
                                

---

## 🎬 Transcript (English)

In the PDF file that we were just working with, I'm going to scroll down to the very bottom page. And done here at the bottom, you'll notice that it mentions that Earth's atmosphere in oceans were formed by volcanic activity and outgassing. Now, as a little exercise, I want to try to ask Claude a very simple question. I want to ask it how Earth's atmospheres and oceans were formed. And I would probably expect to see some kind of answer that says something like volcanic activity and outgassing. So I'm going to copy this right here and put it into my prompt, and ask Claude. Power, Earth's atmosphere and oceans formed. Now, I'm going to run this really quick. And for me at least, I'll notice that in the very first sentence here, I'm given a very appropriate answer. I'm told that these were formed by volcanic activity and outgassing. So that's really exactly what I would expect. But I want you to imagine getting this answer from the perspective of a user. When a user sees this generated text, they might think that it's just Claude speaking directly from memory here. And the user might not really understand that we are actually citing some kind of source here. In this case, the source is not perfect. It is Wikipedia, but at least it is something. So what would be really fantastic is if there was some kind of way to somehow inform the user or tell them how we are getting this information. Luckily, Claude has access to a feature called Citations. Citations allow Claude to refer to some outside source of information directly and say that it got its answer by looking at some other document or some other source of text. Now, let me show you how citations work because once you see it in action, I think you'll have a really good idea of what's going on. I'm going to scroll up to our prompt right here, and I'm going to make a little modification to the first block that we're putting into this message. Right after the source field, I'm going to add in a title of earth.pdf because that is the name of the PDF file that we are opening and a citations field that will be a dictionary with enabled true, like so. Now I'm going to send off this request again. And let's see what we get back now. Now we're going to see that our response is much more complicated than it was previously. Our content field right here is a list that has some text blocks and some of these text block things have a citations list with something called a citation page location. So let's focus on exactly what a citation page location is for just a moment. Let's show you a diagram. A citation page location is Claude's way of telling us exactly where it got some fact or some piece of information from. So in our case, we got back a structure that has a cited text, document index, document title, start page, and end page. The cited text is the text out of the source document, in our case, earth.pdf, that is somehow supporting Claude's statement. The document index and the document title tell us exactly where this statement was made, and the start and end page tell us exactly where inside of that document that statement was made. Now, the real intent behind giving you these citations is to allow you to build up a user interface that looks something like this out of Claude's answer. So I took the response that we just got out of Claude. I fed it back into Claude and asked it to render that entire response in a nicely formatted document and give me some popups to represent all the different citations. But now if I mouse over the one or the two or the three, I'll see a nicely formatted popup appear. This popup contains all the information out of that citation page location object. It is meant to inform the user that Claude's response here, specifically this sentence, really, is being informed by some outside document. So in this case, this sentence is coming from earth.pdf, specifically some text on pages four to five, and the actual text that we're citing is earth's atmosphere was, et cetera, et cetera. So this entire citations feature allows you to build up interfaces like this where a user can be assured that the information being presented by Claude is coming from some actual outside source. The user can then go and refer to that source and make sure that Claude is correctly interpreting the information inside that outside document. This citations feature is not restricted to only being used with PDF documents. You can also use it with plain text as well. So as a very quick example, in the cell right above, I manually copy pasted in some text out of the PDF document, and I assigned it to a variable of article text. Now I can go back down to where I'm making my request down here, and I'm going to make a big update to this block. I'm going to leave the type of document. I'm going to leave this source, but I'm going to change the type to be text. I'm going to change the media type to be text slash plain, and then the data. to be article. So that is the text. That was, oh, sorry, it's article text. There we go. So that's the text that I assigned to that variable up there. I'm then going to change the title to how about something like earth article, since it's not really directly a PDF file anymore. And then I can leave the enabled true with citations in there. So now if I run this again, and take a look at the response, we will see that instead of a citation page location, now we get a citation chart location. So this is going to give us a position inside of that big block of text that Claude is citing from. We can now use this to build up a very similar interface to the one I just showed you inside the browser. So again, you can cite from plain text or PDF documents. Either way, I really recommend you make use of the citations feature anytime that it's critical to make sure that users can somehow investigate how Claude is building up its response and ensure that Claude is drawing information from some source documents, either a PDF or plain text.

---

## 🎬 トランスクリプト（日本語）

先ほど作業していたPDFファイルで、下にスクロールします。 一番下のページまで。そして、この一番下の方に、 地球の大気と海洋が火山活動とガス放出によって形成されたと記載されていることに気づくでしょう。 地球の大気と海洋が形成された。 さて、簡単な演習として、Claudeに質問してみます。 地球の大気と海洋がどのように形成されたかという非常に簡単な質問です。 そして、おそらく火山活動やガス放出といったような答えが返ってくるだろうと予想します。 火山活動 やガス放出のような答えが返ってくると予想します。なので、これをコピーして プロンプトに入れて、Claudeに質問します。「パワー、 地球の大気と海洋が形成された。」さて、 これを実行してみます。私にとっては、 最初の文で、非常に適切な答えが返ってきます。 これらのものが火山活動とガス放出によって形成されたと示されます。 それはまさに私が期待していた通りです。しかし、皆さんに想像してほしいのは、 ユーザーの視点からこの答えを得ることです。 ユーザーがこの生成されたテキストを見たとき、 それは単にClaudeが記憶から直接話していると思っているかもしれません。そして ユーザーは、私たちが何らかの 情報源を引用していることを実際には理解していないかもしれません。 この場合、情報源は完璧ではありません。 Wikipediaですが、少なくとも何かです。 ですから、もし素晴らしいことがあるとすれば、 ユーザーに通知したり、どのように 情報を得ているかを伝えたりする方法があることです。幸いなことに、Claudeは 引用という機能にアクセスできます。引用は Claudeが外部の情報源を 参照し、その答えを 他の文書や他のテキスト情報源を見て得たと言えるようにします。 では、引用がどのように機能するかをお見せしましょう。 一度見れば、何が起こっているのかをよく理解できると思います。上にスクロールして プロンプトまで戻り、少し変更を加えます。 メッセージに入力する最初のブロックに ソースフィールドの直後に、 earth.pdfというタイトルを追加します。 なぜなら、それが開いているPDFファイルの名前だからです。そして 引用フィールドを追加します。これは辞書で、 有効をtrueに設定します。 このように。 もう一度このリクエストを送信します。 そして、何が返ってくるか見てみましょう。今度は、私たちの応答が 以前よりもはるかに複雑になっているのがわかります。私たちの コンテンツフィールドは、テキストブロックを含むリストです。 そして、これらのテキストブロックの一部には 引用リストがあり、引用ページ ロケーションというものがあります。ですから、ちょうど 引用ページロケーションが何であるかに焦点を当てましょう。 少しの間、図をお見せします。引用ページロケーションは Claudeがどこから情報を得たのかを正確に私たちに伝える方法です。 ですから、私たちのケースでは、構造が返ってきました。 引用テキスト、ドキュメントインデックス、ドキュメントタイトル、 開始ページ、終了ページが含まれています。引用テキストは ソースドキュメント、つまり私たちの場合はearth.pdfから Claudeの発言を支持するテキストです。 ドキュメントインデックスとドキュメントタイトルは、どこで この発言がなされたかを正確に教えてくれます。そして、開始ページと終了ページは そのドキュメントのどこで この発言がなされたかを正確に教えてくれます。さて、実際の意図は これらを皆さんにお見せすることです。 Claudeの応答からこのようなユーザーインターフェースを構築できるようにすることです。 ですから、私はClaudeから得た応答を取り、それを Claudeに戻して、その応答全体を整形された ドキュメントとしてレンダリングし、 引用を表すポップアップをいくつか提供するように依頼しました。 しかし今、一つ、二つ、三つにマウスオーバーすると、きれいにフォーマットされたポップアップが表示されます。 マウスオーバーすると、 きれいにフォーマットされたポップアップが表示されます。 このポップアップには、引用ページロケーションオブジェクトの すべての情報が含まれています。それはユーザーに Claudeの応答、特にこの文が 外部の文書から情報を得ていることを知らせるためのものです。 ですから、この場合、この文はearth.pdfから来ています。 具体的には、ページ4から5のテキストで、 そして、引用している実際のテキストは、地球の大気は、 etcétera、 etcéteraです。ですから、この引用機能全体が このようなインターフェースを構築できるようにします。ユーザーは Claudeによって提示されている情報が 実際の外部情報源から来ていることを保証できます。 ユーザーはその後、その情報源を参照し、Claudeが その外部ドキュメント内の情報を正しく解釈しているかを確認できます。 この引用機能は、 PDFドキュメントのみで使用されるわけではありません。 プレーンテキストでも使用できます。 ですから、非常に簡単な例として、上のセルでは、 PDFドキュメントからテキストをコピー＆ペーストして、 article textという変数に割り当てました。 さて、ここで下のほうの要求を作成する場所に戻り、 このブロックを大きく更新します。 ドキュメントの種類はそのままにします。 ソースもそのままですが、種類をテキストに変更します。 メディアタイプをtext/plainに変更し、 そしてデータを articleにします。つまり、それはテキストです。 それは、ああ、すみません、article textです。これで、上の変数に割り当てたテキストです。 次に、タイトルを、そうですね、 earth articleにしましょう。これは実際には直接 PDFファイルではなくなったためです。そして、有効を trueに設定し、引用を含めることができます。ですから、これで もう一度実行し、応答を見てみると、 応答を見てみると、 引用ページロケーションの代わりに 引用チャートロケーションが得られます。 これは、その大きなテキストブロックのどこから Claudeが引用しているのかを示す位置を提供します。 これを使って、先ほどお見せしたのと非常によく似たインターフェースを ブラウザ内で構築できます。ですから、再び、プレーンテキストでも PDFドキュメントからでも引用できます。どちらの場合も、 Claudeがどのように応答を構築しているかをユーザーが調査できるようにし、 Claudeが情報源から情報を引き出していることを保証することが 重要である場合は、引用機能を利用することを強くお勧めします。 Claudeが情報源から情報を引き出していることを保証します。 ユーザーは、PDFまたはプレーンテキストのどちらかである情報源ドキュメントを参照して、Claudeが その外部ドキュメント内の情報を正しく解釈しているかを確認できます。
