# 48. Implementing the RAG flow

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287761
**Section:** 07 RAG and Agentic Search

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    1
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Implementing the RAG flow
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Now that we understand the RAG flow conceptually, let's implement it step by step. We'll walk through a complete example that demonstrates how to chunk text, generate embeddings, store them in a vector database, and perform similarity searches.

The Five-Step RAG Implementation

Our implementation follows the same five steps we discussed previously:

Chunk the text by section
Generate embeddings for each chunk
Create a vector store and add each embedding to it
Generate an embedding for the user's question
Search the store to find the most relevant chunks

This diagram shows how we transform user queries into embeddings and search our vector database to find the most relevant content.

Step 1: Chunking the Text

First, we load our document and split it into manageable sections:

with open("./report.md", "r") as f:
    text = f.read()

chunks = chunk_by_section(text)
chunks[2]  # Test to see the table of contents

We use the same chunk_by_section function from earlier to split our document into logical sections.

Step 2: Generate Embeddings

Next, we create embeddings for all our chunks at once:

embeddings = generate_embedding(chunks)

The embedding function has been updated to handle both single strings and lists of strings, making it more efficient for batch processing.

Step 3: Store in Vector Database

Now we create our vector store and populate it with embeddings and their associated text:

store = VectorIndex()

for embedding, chunk in zip(embeddings, chunks):
    store.add_vector(embedding, {"content": chunk})

Notice that we store both the embedding and the original text content. This is crucial because when we search later, we need to return the actual text, not just the numerical embedding values.

Why Store the Original Text?

When we query our vector database, getting back just the embedding numbers isn't useful. We need the actual text that was used to generate those embeddings. That's why we include the original chunk text (or at least a reference to it) alongside each embedding in our database.

Step 4: Process User Queries

When a user asks a question, we generate an embedding for their query:

user_embedding = generate_embedding("What did the software engineering dept do last year?")

Step 5: Find Relevant Content

Finally, we search our vector store to find the most similar chunks:

results = store.search(user_embedding, 2)

for doc, distance in results:
    print(distance, "\n", doc["content"][0:200], "\n")

This search returns the two most relevant chunks along with their similarity scores (cosine distances).

The search results show us which sections of our document are most relevant to the user's question, along with similarity scores.

Understanding the Results

When we run our example query about the software engineering department, we get back:

Section 2: Software Engineering with a distance of 0.71 (closest match)
Methodology section with a distance of 0.72 (second closest)

Lower distance values indicate higher similarity, so Section 2 is the most relevant to our query.

What's Next?

This implementation works well for basic cases, but there are scenarios where it doesn't perform as expected. In the next sections, we'll explore improvements to make our RAG system more robust and accurate.

The key takeaway is that RAG is fundamentally about converting text to numbers (embeddings), storing those numbers efficiently, and then using mathematical similarity to find relevant content when users ask questions.
                            
                        
                    

                    
                        
                            Downloads
                            
                                
                                    
                                        
         

---

## 🎬 Transcript (English)

Now that we understand the entire RAG flow, we're going to walk through an example inside of another notebook called 003 VectorDB. So in this notebook, I've provided a sample implementation of a vector database. And I've called it Claude vector index right here. If you want to, feel free to take a glance at it, but I'll walk through everything you need to understand about it. Now in this notebook, we're going to walk through the entire RAG flow by implementing five different steps. The same five steps we just spoke about in the last video. So let's get to it. Step number one, I have already opened up the file and read the text from it, specifically our report.md file, which should be in the same directory as the notebook. So in step one, we're going to chunk the text by section. I've already added in a function to help with that. So the same chunk by section function we had previously. So to do our chunking, chunking process, I'll say chunks is chunk by section and pass in all that text. And now just to test things out and make sure I've got everything working correctly, I'll try printing out chunks at index two. And I should see a printout of the table of contents. And then if I go to index three, I should see the next section down and then the next section and so on. Then, on to step two. In step two, we're going to create an embedding for each chunk. Now, just so you know, I rewrote the embedding function slightly so that now we can pass in either a single string or a list of strings. And if we pass in a list of strings, it will create an embedding for each of them and then return that as a list of embeddings. So to implement step number two, we will call generate_embedding and pass in all the chunks and then assign the result to embeddings. Next up, in step three, we are going to create an instance of the vector store. Once the store has been created, we will then loop over all the different pairs of chunks and embeddings. We're going to zip them together, and then as we take each pair, we're going to insert them into the store. We'll do that with a for embedding, chunk in zip(embeddings, chunks). And again, for each of those different pairs of embeddings and chunks, we'll do a store.add(vector=embedding, metadata={"content": chunk}). the embedding in. And then as the second argument, we'll put in a dictionary with content of chunk. Now, I went over this step rather quickly. So let's do a quick aside and explain why we are looping over all these things, why we were chunking it, and why we were adding in this extra dictionary with the content of chunk. As we just discussed, eventually at some point in time, we're going to reach out to our vector database and give back a list of all the different related embeddings to the input. Now, when we get back this list right here, just getting the number by itself, just getting the embedding is not really useful to us because the embedding doesn't really have a lot of meaning to you and I as developers. What we really care about is the text associated with that embedding. So usually whenever you store these different embeddings inside of your vector database, you're also going to include either the text from the chunk that the embedding was generated from, or at least the ID of the chunk, something to at least point you back to the original chunk text. So in this case, I'm going to include the original chunk text along with each embedding. Again, just so when we do the look-up later on, and I get back the most similar chunks, I've got the actual text that I'm looking for. Now onto step four. So in step four, at some point in time in the future, a user is going to ask us a question. We need to take that question and generate an embedding for it. So we'll make a user embedding by calling generate_embedding. And then my question here, is going to be what did the software engineering department do last year. Finally, on step five, where we are going to try to find some relevant documents. So I want to search the store with the embedding and I want to find the two most relevant chunks, not just the most relevant. I want to get the two chunks that seem to be most relevant to this question right here. So for that, I'll do a results = store.search( I'm going to pass in the user embedding and I'm going to pass in another argument here of two because I want to find the two most relevant chunks. And then I will print out for doc, distance in results: I'm going to print out the distance, a new line, and then the document's content. And because each chunk here is really, really large, I'm going to print out just the first 200 characters. And then another new line like so. And I'll run this. And there's our result. So we get back section two as our best result. We also see the cosine distance here. So it's 0.71. And the next closest chunk is at .72, and that was the methodology section. So these were the two chunks that were found most relevant for the user query that we just submitted. All right, so that is our entire RAG workflow. Now all this works, but there is one or two scenarios where everything doesn't quite work as expected. So there are still a couple of improvements that we could add into our workflow, and let's start to discuss those in just a moment.

---

## 🎬 トランスクリプト（日本語）

これでRAGフロー全体を理解したので、 003 VectorDBという別のノートブック内で例を walkthrough します。 なので このノートブックでは、サンプルの実装を提供しました。 ベクターデータベースの。そしてクロードと呼びました ベクターインデックスをここに。ご希望であればどうぞ glance してみてください。しかし、必要なことはすべて説明します。 それを理解することです。さて、このノートブックでは、 5つのステップを実装して、RAGフロー全体を walkthrough します。 直前のビデオで説明したのと同じ5つのステップです。 では始めましょう。 ステップ1、ファイルを既に開いて テキストを読み込みました。具体的にはレポート.mdファイルです。 これはノートブックと同じディレクトリにあるはずです。 それで、ステップ1では、テキストをセクションごとに チャンク化します。そのための関数を既に追加しました。 なので、以前のセクションごとのチャンク化関数と同じです。 チャンク化、チャンク化プロセスを実行するために、 チャンクをセクションごとにチャンク化します。 と呼び、すべてのテキストを渡します。そして すべてが正しく動作していることを確認するために、 インデックス2のチャンクを印刷してみます。 そして、目次が出力されるはずです。 次にインデックス3に行くと、次のセクションが表示され、 そしてその次のセクションが表示されるはずです。 そしてそのように続きます。 次に、 ステップ2に進みます。ステップ2では、各チャンクに 埋め込みを作成します。さて、お知らせですが、埋め込み関数を 少し書き直したので、単一の文字列または文字列のリストを 渡すことができるようになりました。 そして文字列のリストを渡した場合、それぞれに埋め込みを作成し、 それを埋め込みのリストとして返します。 したがって、ステップ2を実装するために、 generate_embedding を呼び出し、 すべてのチャンクを渡して、結果を埋め込みに割り当てます。 次に、ステップ3では、 ベクターストアのインスタンスを作成します。 ストアが作成されたら、すべての異なるチャンクと埋め込みのペアを ループします。それらを一緒にzipし、 各ペアを取得しながら、それらをストアに挿入します。 これを for embedding, chunk in zip(embeddings, chunks) で行います。そして 埋め込みとチャンクの各ペアに対して、 store.add(vector=embedding, metadata={"content": chunk}) を実行します。 埋め込みを格納します。そして2番目の引数として、 チャンクのコンテンツを持つ辞書を入れます。 このステップはかなり駆け足で説明しましたが、少し寄り道して なぜこれらのすべてをループしているのか、なぜチャンク化しているのか、 そしてなぜこの追加の辞書をチャンクのコンテンツとともに 追加しているのかを説明しましょう。先ほど説明したように、 いずれはベクターデータベースに問い合わせて、関連する すべての埋め込みのリストを返すことになります。 このリストを受け取ったとき、単に数値だけでは、 埋め込み自体は、私たち開発者にとってあまり意味がありません。 本当に私たちが気にかけているのは、その埋め込みに関連する テキストです。そのため、通常は これらの埋め込みをベクターデータベースに格納する際には、 埋め込みが生成されたチャンクのテキスト、 または少なくともチャンクのIDを含めて、 元のチャンクテキストを指し示すものを格納します。 そのため、この場合は元のチャンクテキストを 各埋め込みとともに含めます。 後で検索するときに、最も類似したチャンクを取得できるように、 探している実際のテキストを持てるようにするためです。 では、ステップ4に進みます。 ステップ4では、将来のある時点で、ユーザーが 質問をすることになります。その質問を受け取って、 その質問の埋め込みを生成する必要があります。 したがって、generate_embedding を呼び出して、 ユーザー埋め込みを作成します。 そして私の質問は、 ソフトウェアエンジニアリング部門が昨年何をしたか ということです。最後に、 ステップ5では、関連するドキュメントを検索します。 それで、ストアを検索したいのですが、 埋め込みを使用して、最も関連性の高い 2つのチャンクを見つけたいのです。最も関連性の高いものだけでなく。 この質問に最も関連していると思われる 2つのチャンクを取得したいのです。 そのため、store.search を使用します。 そして、 ユーザー埋め込みを渡して さらに2という引数を渡します。なぜなら、 最も関連性の高い2つのチャンクを見つけたいからです。 そして、結果を印刷します。 doc, distance in results: 距離、改行、そして ドキュメントのコンテンツを印刷します。 各チャンクは非常に大きいため、 最初の200文字だけを印刷します。 そして、その後も改行します。 そして実行します。結果が出ました。 セクション2が最も良い結果として返されました。 コサイン距離も表示されています。 0.71です。そして次に 近いチャンクは0.72で、 方法論のセクションでした。これらは、 送信したばかりのユーザーの質問に対して 最も関連性が高いと見なされた2つのチャンクです。 さて、これが私たちのRAGワークフロー全体です。 すべてうまく機能しますが、 期待どおりにすべてが機能しないシナリオがいくつかあります。 したがって、ワークフローに追加できる 改善点がいくつかあります。 すぐに議論を始めましょう。
