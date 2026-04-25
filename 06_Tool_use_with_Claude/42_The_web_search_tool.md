# 42. The web search tool

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287755
**Section:** 06 Tool use with Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    2
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    The web search tool
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Important note: Your organization must enable the Web Search tool in the settings console before using it. You can find this setting here: https://console.anthropic.com/settings/privacy
Claude includes a built-in web search tool that lets it search the internet for current or specialized information to answer user questions. Unlike other tools where you need to provide the implementation, Claude handles the entire search process automatically - you just need to provide a simple schema to enable it.

Setting Up the Web Search Tool
To use the web search tool, you create a schema object with these required fields:
web_search_schema = {
    "type": "web_search_20250305",
    "name": "web_search", 
    "max_uses": 5
}
The max_uses field limits how many searches Claude can perform. Claude might do follow-up searches based on initial results, so this prevents excessive API calls. A single search returns multiple results, but Claude may decide additional searches are needed.
How the Response Works
When Claude uses the web search tool, the response contains several types of blocks:

Text blocks - Claude's explanation of what it's doing
ServerToolUseBlock - Shows the exact search query Claude used
WebSearchToolResultBlock - Contains the search results
WebSearchResultBlock - Individual search results with titles and URLs
Citation blocks - Text that supports Claude's statements

The response structure lets you see exactly what Claude searched for and which sources it found. Citations include the specific text Claude used to support its answers, along with the source URLs.
Restricting Search Domains
You can limit searches to specific domains using the allowed_domains field. This is particularly useful when you want reliable, authoritative sources:
web_search_schema = {
    "type": "web_search_20250305",
    "name": "web_search",
    "max_uses": 5,
    "allowed_domains": ["nih.gov"]
}
For example, when asking about medical or exercise advice, restricting to domains like PubMed (nih.gov) ensures you get evidence-based information rather than random blog content.

Rendering Search Results
The different block types in the response are designed for specific UI rendering:

Render text blocks as regular content
Display web search results as a list of sources at the top
Show citations inline with the text, including the source domain, page title, URL, and quoted text

This structure helps users understand how Claude arrived at its answers and provides transparency about the sources being used. The citation format makes it clear which specific information came from which sources, building trust in the AI's responses.
Practical Usage
The web search tool works best for:

Current events and recent developments
Specialized information not in Claude's training data
Fact-checking and finding authoritative sources
Research tasks requiring up-to-date information

Simply include the schema in your tools array when making API calls, and Claude will automatically decide when a web search would help answer the user's question.
                            
                        
                    

                    
                        
                            Downloads
                            
                                
                                    
                                        
                                            
                                            
                                                006_web_search.ipynb
                                                (opens in new tab)
                                            
                                        
                                    
                                
                                    
                                        


---

## 🎬 Transcript (English)

There's another tool built directly into Claude named the web search tool. As the name implies, this tool allows Claude to search the web for up-to-date or specialized information to answer a user's question. For example, if we ask about current events in quantum computing, Claude might decide to use this tool to find some up-to-date articles related to quantum computing and then use that content to formulate an answer. Unlike the text editor tool, we do not have to provide an implementation to actually run the search. The search is done entirely by Claude, and this makes this tool really easy to run and use. Let's write out some code to understand how this tool works. I'm back inside of a notebook. I've created a new one called 006 web search. And I've got a cell down here at the bottom with some typical code for running a request off to Claude. In the cell right above, I'm going to create a new variable called web search schema. This is going to be a schema that we author that we are going to include in our request off to Claude, and we're going to list it as a tool. This schema is going to enable the web search functionality. So just like the text editor tool, we have to provide this very small schema that behind the scenes is going to get expanded into a much larger schema. We're going to add in a couple of fields here, in particular a type with web search_2025-03-05 then a name of web_search, a max uses of five, and that's it for right now. Now the max uses is the number of times that Claude can run a search. A single search can return multiple different search results, but depending upon the content in those search results, Claude might decide to do a follow-up research. This process can repeat several times, so we are capping the number of times that Claude can search in total to just five. I'm going to go down here after running that cell. And I'm going to ask Claude what's the best exercise for gaining leg muscle. And I'm going to add in that schema that we just put together. So web search schema like so. Now I'm going to run this, and it's going to take a little bit of time to get a response back. The response we get back is going to be quite large, so I can scroll through it here, and we're going to see that there is just a tremendous amount of information here. So to help you understand the response we got back, I want to show you a little part-down version of this response, where I took this messages, content list, and I removed a ton of content out of it just so we can better understand what is going on. So here is a slightly redacted form. Again, this is the content list inside the response message. The content list is going to contain several different blocks, several blocks we have not seen before. Initially, we get back a text block, which is kind of framing the entire response that Claude is giving us. Claude is saying that it's going to do a web search to better understand how to answer the question. Then we're going to see a server tool use block. And inside there is the input to the search tool. We can see that's the exact query that Claude is going to use to search the web. After that, we're going to see a listing of web search tool result block, and inside there are going to be many different web search result block. These are the different search results that Claude has received from that initial query. Now, an actual query response will probably have many different search results. In this case, I removed all of them, but one, just to better understand what's going on here. So this is an actual web search result. We can see the title of the page that Claude fetch, and the actual URL. There's no content inside of here just yet. This is just telling us exactly what Claude found when it did this search. Then Claude is going to begin by answering the user's question. And it's going to answer the user's question with a variety of different text blocks that might include a citations list. The citations list is text that is supposed to support the statements that Claude is making in some way. So in this case, Claude has cited some particular web page right here. And it is using this specific text to support the point or the argument that it's trying to make. When we define the web search schema, there are a variety of different fields that we can add in. There's one field in particular that I really recommend you consider using if you ever have a good understanding of exactly what your users are going to be asking about. So in our case, we asked about the best leg exercises for gaining leg muscle. I don't know if you've ever searched online for exercise advice, but there are a tremendous number of blogs out there with probably just AI-generated content. And the advice that you get out of those blogs might not actually be the most accurate, or even the best idea of how to actually gain leg muscle. On the other hand, there are some websites that collect different publications such as PubMed. So this is a website maintained by the US government. It contains a ton of different scholarly articles around medicine. So we could search through here and find a tremendous amount of evidence-supported exercise advice. So it would be really fantastic if we could somehow tell Claude to only search this web page and content inside of it. That would allow us to make sure that we are giving the best possible advice to our users and not just some randomly generated stuff that we found online. In order to get Claude to only search this page, we're going to find the domain, which is nih.gov. I'm going to go back over to my notebook. I'm going to find my web search schema, and I'm going to add in an additional field here of allowed domains. I'm going to put in a list with NIH.gov. This is going to constrain Claude Search to only that domain right there, and it won't try to find anything else. So now if I run this cell again, and then make my request off to Claude again, I'm going to have to wait for the response to come back. But when we do get a response, we should be able to scroll through it a little bit and eventually see that we have a URL right here. And we should only have URLs belonging to the NIH.gov domain. We shouldn't see anything else. So again, this will allow us to make sure that we are giving at least some scientifically supported advice to our users. Now, last thing I'm going to do is show you exactly how we are really intended to use this giant list of different types of blocks that we get back when we make use of this tool. The thought process here is that you're going to render all the text blocks as plain text, and then whenever you get a web search result block or a citation web search result location, you might render those out inside the UI in such a way that makes it obvious to a user that you are trying to support your information in some way. Here's an example of how you might do that. I wrote out a small page that is going to take all those different blocks we saw inside the response message and render them out. At the very top right here, I've got a list of all my web search tool result blocks. So these are the different pages that Claude found when it did the web search. I'm then going to iterate through the entire list of blocks and show the text out of every single text block. Whenever I found a text block that has a citation web search result location, I know that's a long term, so it's one of these right here. Whenever I find one of those, I might render it with a little citation like so, where I'll show the domain, show the title of the page that I found, show the exact address of it, and then the exact cited text as well. Again, this just allows our users to better understand how Claude is actually getting its information.

---

## 🎬 トランスクリプト（日本語）

Claude には、Web 検索ツールという別のツールも組み込まれています。 名前の通り、このツールを使うと Claude は Web を検索して 最新情報や専門的な情報をユーザーの質問に答えるために利用できます。 例えば、量子コンピューティングの最新の出来事について質問した場合、 Claude はこのツールを使用して、量子コンピューティングに関連する 最新の記事を見つけ、その情報を使って回答を生成するかもしれません。 テキストエディタツールとは異なり、検索を実行するための実装を 提供する必要はありません。検索はすべて Claude が行うため、 このツールは非常に簡単に実行して使用できます。 このツールの仕組みを理解するために、コードを書いてみましょう。 新しいノートブックを作成し、「006 web search」と名付けました。 一番下のセルには、Claude にリクエストを送信するための一般的なコードがあります。 そのすぐ上のセルで、「web search schema」という新しい変数を作成します。 これは、Claude へのリクエストに含めるスキーマであり、 ツールとしてリストします。このスキーマは Web 検索機能を有効にします。テキストエディタツールと同様に、 裏でより大きなスキーマに拡張される、非常に小さなスキーマを 提供する必要があります。 ここではいくつかのフィールドを追加します。 特に type は `web search_2025-03-05`、 name は `web_search`、`max_uses` は 5 です。 今のところは以上です。 `max_uses` は Claude が検索を実行できる回数です。 1 回の検索で複数の検索結果が得られることもありますが、 それらの検索結果の内容によっては、Claude はさらに調査を行うことを決定するかもしれません。 このプロセスは数回繰り返される可能性があるため、Claude が合計で検索できる回数を 5 回に制限しています。 そのセルを実行した後、下に移動して、 Claude に「脚の筋肉を鍛えるのに最適な運動は何ですか？」と尋ねます。 そして、先ほど作成したスキーマを追加します。 `web search schema` のように。 これを実行します。応答が返ってくるまで少し時間がかかります。 返ってくる応答はかなり大きくなるため、スクロールできます。 ここに大量の情報があることがわかります。 応答を理解しやすくするために、応答の抜粋バージョンを少し表示します。 メッセージのコンテンツリストから多くのコンテンツを削除しました。 応答の redacted バージョンを次に示します。 これは、応答メッセージ内のコンテンツリストです。 コンテンツリストには、これまで見たことのないいくつかのブロックが含まれます。 まず、Claude が提供する応答全体をフレーム化するテキストブロックがあります。 Claude は、質問に答えるために Web 検索を行うと述べています。 次に、ツール使用ブロックが表示されます。 その中には、検索ツールの入力があります。 これは Claude が Web を検索するために使用する正確なクエリです。 その後、Web 検索ツール結果ブロックのリストが表示されます。 その中には、多くの Web 検索結果ブロックが含まれます。 これらは、Claude が初期クエリから受け取ったさまざまな検索結果です。 実際のクエリ応答には、複数の検索結果が含まれる可能性が高いです。 ここでは、1 つを除いてすべて削除しましたが、 内容をより理解しやすくするためです。 これは実際の Web 検索結果です。Claude が取得したページのタイトルと 実際の URL を見ることができます。 まだコンテンツはありません。これは Claude が検索時に何を見つけたかを示しているだけです。 次に、Claude はユーザーの質問に答え始めます。 そして、引用リストを含むさまざまなテキストブロックで質問に答えます。 引用リストは、Claude が述べている内容を 何らかの方法でサポートするためのテキストです。 この場合、Claude は特定の Web ページを引用しています。 そして、この特定のテキストを使用して、主張や論点を サポートしています。 Web 検索スキーマを定義する際に、追加できるさまざまなフィールドがあります。 ユーザーが何を尋ねるかを正確に理解している場合、特に推奨したいフィールドが 1 つあります。 それは、ユーザーのクエリを絞り込むことができるということです。 私たちの場合は、「脚の筋肉を鍛えるのに最適な運動」について尋ねました。 運動のアドバイスをオンラインで検索したことがある方は、 おそらく AI が生成したコンテンツのブログがたくさんあることに気づくでしょう。 そして、それらのブログから得られるアドバイスは、 実際には最も正確ではないかもしれませんし、 脚の筋肉を鍛えるための最善の方法さえわからないかもしれません。 一方で、PubMed のようなさまざまな出版物を収集しているウェブサイトもあります。 これは米国政府が管理するウェブサイトです。 医学に関する学術論文が多数含まれています。 ここで検索すると、エビデンスに基づいた運動のアドバイスが たくさん見つかります。 そのため、Claude にこの Web ページとそのコンテンツのみを検索するように指示できると、 非常に素晴らしいでしょう。 これにより、オンラインで見つけたランダムに生成されたものではなく、 最善のアドバイスを提供していることを確認できます。 このページのみを検索するように Claude に指示するために、 ドメインである `nih.gov` を見つけます。 ノートブックに戻ります。 Web 検索スキーマを見つけて、追加フィールドとして `allowed_domains` を追加します。 ここに `NIH.gov` のリストを追加します。 これにより、Claude の検索がそのドメインのみに制限され、 それ以外のものは検索しようとしなくなります。 したがって、もう一度このセルを実行し、 Claude にもう一度リクエストを送信すると、応答を待つ必要があります。 しかし、応答が得られたら、少しスクロールして URL を見つけることができるはずです。 そして、URL は NIH.gov ドメインに属するもののみでなければなりません。 それ以外のものは表示されないはずです。 これにより、少なくとも科学的に裏付けられたアドバイスを ユーザーに提供していることを確認できます。 最後に、このツールを使用する際に得られるさまざまなブロックの 巨大なリストを実際にどのように使用するのかを説明します。 ここでは、すべてのテキストブロックをプレーンテキストとしてレンダリングし、 Web 検索結果ブロックや引用 Web 検索結果の場所を受け取った場合は、 UI 内で、ユーザーに情報が何らかの方法でサポートされていることを わかりやすく伝える方法でレンダリングすることを検討できます。 これは、その方法の一例です。 ここでは、応答メッセージ内のすべてのブロックを取得し、 それらをレンダリングする小さなページを作成しました。 ここの最上部には、すべての Web 検索ツール結果ブロックのリストがあります。 これらは、Claude が Web 検索を行った際に見つけたさまざまなページです。 次に、ブロックのリスト全体を反復処理し、すべてのテキストブロックの テキストを表示します。 テキストブロックの中に引用 Web 検索結果の場所がある場合、 それはこれらのブロックのいずれかであることを意味します。 それらのいずれかを見つけた場合、 ドメイン、見つかったページのタイトル、 正確なアドレス、そして引用されたテキストを 表示するなど、引用のような形式でレンダリングできます。 これは、ユーザーが Claude がどのように情報を取得しているかを よりよく理解するのに役立ちます。
