# 47. The full RAG flow

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287764
**Section:** 07 RAG and Agentic Search

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    The full RAG flow
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Now that we've covered the basics of RAG, text chunking, and embeddings, let's walk through the complete RAG pipeline step by step. This example will show you exactly how all these pieces work together to retrieve relevant information and generate responses.

Step 1: Chunk Your Source Text

First, we take our source document and break it into manageable chunks. For this example, we'll use two simple text sections:

Section 1: Medical Research - "This year saw significant strides in our understanding of XDR-47, a 'bug' we have not seen before."
Section 2: Software Engineering - "This division dedicated significant effort to studying various infection vectors in our distributed systems"

Step 2: Generate Embeddings

Next, we convert each text chunk into numerical embeddings using an embedding model. To make this easier to understand, let's imagine we have a perfect embedding model that always returns exactly two numbers, and we know what each number represents.

In our imaginary model:

The first number represents how much the text talks about the medical field
The second number represents how much the text talks about software engineering

For the medical research section, we might get [0.97, 0.34] - very medical-focused but with some software elements due to the word "bug". For the software engineering section, we get [0.30, 0.97] - heavily software-focused but with medical undertones from "infection vectors".

Normalization

The embedding API typically performs a normalization step that scales each vector to have a magnitude of 1.0. You don't need to worry about the math here - it's handled automatically. This gives us normalized vectors like [0.944, 0.331] and [0.295, 0.955].

We can visualize these embeddings on a unit circle, where each point represents one of our text chunks.

Step 3: Store in Vector Database

We store these embeddings in a vector database - a specialized database optimized for storing, comparing, and searching through long lists of numbers like our embeddings.

At this point, we pause. All the work so far has been preprocessing that happens ahead of time. Now we wait for a user to submit a query.

Step 4: Process User Query

When a user asks a question like "I'm curious about the company. In particular, what did the software engineering dept do this year?", we run their query through the same embedding model.

This query gets embedded as something like [0.1, 0.89] - low medical score, high software engineering score. After normalization, we get [0.112, 0.993].

Step 5: Find Similar Embeddings

We send the user's query embedding to our vector database and ask it to find the most similar stored embeddings.

The database returns the software engineering section because it's the closest match to what the user asked about.

How Similarity Works: Cosine Similarity

The vector database uses cosine similarity to determine which embeddings are most similar. This measures the cosine of the angle between two vectors.

Key points about cosine similarity:

Results range from -1 to 1
Values close to 1 mean high similarity
Values close to -1 mean very different
0 means perpendicular (no relationship)

In our example, the cosine similarity between the user query and the software engineering chunk is 0.983 - very high similarity. The similarity with the medical research chunk is only 0.398 - much lower.

Cosine Distance

You'll often see "cosine distance" in vector database documentation. This is simply calculated as (1 - cosine similarity). With cosine distance:

Values close to 0 mean high similarity
Larger values mean less similarity

This adjustment makes the numbers easier to interpret in many contexts.

Step 6: Create the Final Prompt

Finally, we take the user's question and the most relevant text chunk we found, combine them into a prompt, and send it to Claude for a response.

The prompt might look like:

Answer the user's question about the financial document.

<user_question>
How many bugs did engineers fix this year?
</user_question>


---

## 🎬 Transcript (English)

At this point in the module, I've given you a high-level overview of how that rag pipeline works. We've spoken a little bit about text chunking, and we've got just a taste of text embeddings. So now we're going to take these three different topics, our high-level overview of the rag process, text embeddings and text chunking, and we're going to merge them all together and really understand the entire rag pipeline. So we're going to go through a complete rag example and go through a lot of detail and really understand everything step by step. So let's get to it. Step number one, just as before, we're going to take some source document and chunk it into separate pieces of text. So for this example, I'm going to assume I just have two pieces of text here, just section one, medical research, and section two, software engineering. Step two, we're going to generate embeddings for each of these different chunks of text. Now in this example, we're going to pretend that we have this imaginary super perfect embedding model. And this embedding model has two very important characteristics. First, we're going to assume that always returns embeddings of length two, so just two separate numbers. And we're going to also assume that we know exactly what each number is really scoring about the source text. Remember, in reality, that's not the case. But in this scenario, we're going to imagine we know exactly what each number is really talking about. So we're going to say that the first number is how much the text is talking about the medical field, and the second is how much the text is talking about software engineering. So for the first chunk of text, when we embed it, this thing is definitely talking about medical research. So I would give it maybe a score of .97 to say, yes, absolutely, this is very much talking about the medical field. And then it also uses the term bug, which has a slight software engineering connotation. In addition, medical itself is pretty heavy on software engineering. So I'm going to give it a score of .344 software engineering. Then for the second piece of text here. Well, it's definitely talking about software engineering, so I'm going to give it a score of .97 for that. And then it also mentions infection vectors, which has that connotation of medicine. So I'll give it a slightly higher medicine score as well of .3. Now that we have generated these embeddings, We're going to go through an extra little step of mathematics here, something referred to as normalization. Now, you do not really have to understand normalization that much. This is already going to be done for you in the vast majority of cases by the embedding API that you are using. This normalization step is going to scale the magnitude of each of these pairs of vectors to 1.0. And if you don't understand that terminology, totally fine. Don't sweat it too much. Just understand that we're going to do a slight little adjustment to the actual magnitude of each number. Once we have generated these embeddings and normalized them, we can kind of visualize them on a plot like this. So on this plot, I've drawn a unit circle, and each of our points representing both those embeddings will lie exactly on the circle because we have normalized their lengths to exactly one. So we've got the software engineering section up here, and here's medical research over here. So now that we have these embeddings, we're going to move on to the next step. In this step, we are going to take these embeddings and store them inside of something called a vector database. This is a database that has been optimized for storing, comparing, and looking up long lists of numbers exactly like what our embeddings are. Now, at this point in time, we pause, we take a break, because this is all been pre-processing work that we did ahead of time. So at this point, we just sit around and wait for a user to actually submit a query to our application. So we will imagine that at some point in time, finally, a user will come to our app and maybe type into a chatbot or something like that in their question or their query. Maybe in this case, their question is going to be something like, I'm curious about the company, in particular, what did the software engineering department do this year? Now at this point in time, we're going to take that user's question and we're going to run it through the exact same imaginary embedding model. In this scenario, because the user's question is asking specifically about software engineering, I'll give it a score of 0.89. And then because it's also talking about company and again software engineering is kind of tied up in the medical field, I'll give it a very slight medical score as well of 0.1. Now that we have this embedding, we're going to go and go through that normalization step again. And then finally, we're going to make use of our vector database. We're going to take the user's query. We're going to feed it into the vector database and say, please search through all the vectors we have stored inside of you and give us the vector that is closest in nature to this one. So in our case, I would kind of expect to get back Section 2 software engineering because that's kind of what the user asked about over here. But let me tell you exactly what is happening inside of the vector database that is able to give us this very closely related result. Okay, so a little bit of math here, don't worry, won't be too much. So when we take the user's query and add it onto this chart, we can see right away that visually the user's query is just really close to software engineering. So you and I as humans, we could look at this chart and say, oh yeah, clearly these two things are very close. The user's query is very similar to software engineering. So obviously, if we want to find some chunks inside the vector database related to the user query, this would be the one that we want. But of course, we are using computers here. And our computer doesn't actually just make a chart like this and then look at it. There's some actual calculation going on behind the scenes. So let's examine exactly what that calculation is. And it's kind of important for you to know it because eventually when you start using vector databases, they're going to use a lot of terminology that's related to this kind of math going on behind the scenes. And to actually interface well with the vector database, you kind of need to have at least a very basic understanding of the math. So that's why I want you to understand it. All right, here's a high-level look at the map that is being done inside of your vector database. To find which embeddings are most similar to the user's query, we want to calculate something called the cosine similarity. This is the cosine of the angle between the user's query and each of the other embeddings stored in the database. So we'd want to find the angle A, right here, and take the cosine of it, and angle B right here, and take the cosine of it. The math for this is shown on the right-hand side. The result of this calculation will be a number between negative 1 and 1. If we get a result close to 1, as we did right here, then that means that we have found an embedding very similar to the user's query. Results closer to negative 1 mean we have found an embedding that are not at all similar to the user's query. In our case, the cosine similarity between our user query and the software engineering chunk is 0.983, meaning that these two embeddings are very similar. So this is a sign to us that we would want to take the software engineering chunk of text and include it in our prompt with the user's question. Now, before we move on, one other quick thing that's going to be a little confusing right now, but it's going to be very, very helpful to know later on when you start working with vector databases. In a lot of vector database documentation, you're going to see something referred to as a cosine distance. This is different than the cosine similarity. It is calculated as one minus the cosine similarity. As adjustment is often done, just to give us an easier to interpret number. With a cosine distance, values close to zero mean you have a large similarity. And larger values than that mean we have less similarity. Again, this is something you're going to see very often in vector database documentation. So just be aware of it whenever you see the term cosine distance and cosine similarity. So now that we understand some of this math at a very high level, let's get back on track. Once we have found a text chunk with a high similarity to the user's question, we're going to take the user's question, add it into our prompt, and the text chunk that we found that's most relevant and put that into our prompt as well. We then take that prompt and send it off to Claude. And that's the entire process in great, great detail. So now that we understand everything from start to finish with all the kind of tech behind the scenes going on and even some of the math, let's start to implement this inside of a notebook in just a moment.

---

## 🎬 トランスクリプト（日本語）

このモジュールの現時点では、高レベルの概要を説明しました。 そのragパイプラインがどのように機能するかについて。テキストチャンキング について少し話しました。そして、テキスト埋め込み を少しだけ体験しました。そこで今から、これら3つの 異なるトピック、ragの プロセスに関する高レベルの概要、テキスト埋め込み、そしてテキストチャンキングを 取り上げ、すべてを統合して、ragパイプライン全体を 本当に理解します。したがって、 ragの完全な例を通して、多くの詳細を理解し、ステップバイステップで すべてを本当に理解していきます。それでは始めましょう。 ステップ1、いつものように、 ソースドキュメントを取得し、それを別々のテキスト片に チャンク化します。この例では、 ここに2つのテキスト片、セクション1の医療研究と セクション2のソフトウェアエンジニアリングだけがあると 仮定します。ステップ2、これらの異なるチャンクの それぞれに対して埋め込みを生成します。この例では、 この想像上の、非常に完璧な埋め込みモデルがあると 仮定します。そして、この埋め込みモデルには2つの非常に 重要な特徴があります。まず、常に 長さ2の埋め込み、つまり2つの別々の数字を 返すことを想定します。そして、各数字が ソーステキストの何を本当に評価しているのかを 正確に知っていると想定します。現実はそうではないことを 思い出してください。しかし、このシナリオでは、正確に 何が各数字が何を話しているのかを正確に知っていると 想像します。そこで、最初の数字は、テキストが 医療分野についてどれだけ話しているか、 そして2番目の数字は、ソフトウェアエンジニアリングについて どれだけ話しているかだとします。 最初のテキストチャンクの場合、これを埋め込むと、 これは間違いなく医療研究について話しています。なので、 これは医療分野について非常によく話しているということを示すために、 例えば0.97というスコアを付けます。 そして、用語のバグも使用していますが、これは ソフトウェアエンジニアリングにわずかに関連しています。さらに、 医療自体もソフトウェアエンジニアリングにかなり 関連しています。なので、ソフトウェアエンジニアリングの スコアは0.344とします。次に、2つ目の テキストについてです。これは間違いなくソフトウェア エンジニアリングについて話しているので、そのスコアは0.97とします。そして 感染経路についても言及しています。これは 医学のニュアンスがあります。なので、 医療のスコアも0.3と少し高くします。 これらの埋め込みを生成したので、 次に、数学の追加のステップを 進めます。正規化と呼ばれるものです。 正規化についてはそれほど理解する必要はありません。 ほとんどの場合、使用している埋め込みAPIによってすでに処理されます。 この正規化ステップは、これらの各ベクトルのペアの 大きさを1.0にスケーリングします。もし その専門用語を理解できなくても、全く問題ありません。あまり気にしないでください。 単に各数字の実際の大きさにわずかな調整を行うとだけ理解してください。 これらの埋め込みを生成し、正規化した後、 このようなプロットで視覚化することができます。 このプロットでは、単位円を描いており、これらの埋め込みを表す 各点が円上に正確に配置されます。なぜなら、 正規化後の長さが正確に1になるからです。 ソフトウェアエンジニアリングのセクションはここにあり、 医療研究はここにあります。 これらの埋め込みができたので、次のステップに進みます。 このステップでは、これらの埋め込みを取得し、 ベクトルデータベースと呼ばれるものに保存します。これは、 長い数字のリストの保存、比較、検索に最適化されたデータベースです。 まさに私たちの埋め込みがそうであるように。 さて、この時点で一時停止し、休憩を取ります。なぜなら、これらは すべて事前に準備した前処理作業だからです。 この時点で、ユーザーがアプリケーションにクエリを送信するのを待ちます。 ユーザーがチャットボットなどに 質問やクエリを入力するのを待ちます。この場合、 例えば、「会社について、特にソフトウェアエンジニアリング部門が 今年何をしたのか知りたい」という質問かもしれません。 この時点で、そのユーザーの質問を取得し、 同じ想像上の埋め込みモデルを実行します。 このシナリオでは、ユーザーの質問は特にソフトウェアエンジニアリングについて 尋ねているため、0.89というスコアを付けます。 そして、会社についても話しているので、またソフトウェアエンジニアリングは 医療分野と少し関連しているので、医療のスコアも 0.1と非常にわずかにします。 この埋め込みができたら、正規化ステップをもう一度実行し、 そして最後にベクトルデータベースを活用します。 ユーザーのクエリを取得し、ベクトルデータベースに渡し、 そこに保存されているすべてのベクトルを検索して、 これに最も近いベクトルを返してくださいと言います。 私たちの場合は、セクション2のソフトウェアエンジニアリングが 返されると予想されます。なぜなら、それがユーザーが尋ねたことだからです。 しかし、ベクトルデータベース内で何が起こって、 この非常に関連性の高い結果を返せるのかを正確に説明します。 さて、ここでも少し数学をします。心配しないでください、それほど多くはありません。 ユーザーのクエリを取得してこのチャートに追加すると、 すぐに視覚的にユーザーのクエリが ソフトウェアエンジニアリングに非常に近いことがわかります。 だから私たち人間は、このチャートを見て、「ああ、確かにこれらの2つは 非常に近い。ユーザーのクエリはソフトウェアエンジニアリングに 非常に似ている。」と言うことができます。だから当然、 ベクトルデータベース内のユーザークエリに関連するチャンクを見つけたいなら、 これが私たちが欲しいものです。 しかしもちろん、私たちはコンピューターを使っています。そしてコンピューターは 実際にはこのようなチャートを作成して見るわけではありません。裏側では 計算が行われています。なので、その計算が 何であるかを正確に見ていきましょう。そして それはあなたが知っておくべきことです。なぜなら最終的に ベクトルデータベースを使用する場合、それらは多くの用語を使用するからです。 それは裏側で行われているこの種の数学に関連しています。そして実際に ベクトルデータベースと効果的に連携するには、 少なくとも数学の非常に基本的な理解が必要だと思います。 だからこそ、それを理解してほしいのです。わかりました、ここに ベクトルデータベース内で何が行われているかについての 高レベルの概要があります。ユーザーのクエリに 最も似ている埋め込みを特定するために、 コサイン類似性と呼ばれるものを計算します。これはユーザーのクエリと データベースに保存されている他の各埋め込みの 間の角度のコサインです。なので、 角度A、ここの角度を取り、 そのコサインを取り、そして角度B、ここの角度を取り、 そのコサインを取ります。そのための数学は右側に示されています。 この計算の結果は、マイナス1から1の間の数字になります。もし結果が1に近い場合、 ここでそうであったように、それはユーザーのクエリに非常に似ている 埋め込みを見つけたことを意味します。マイナス1に近い結果は、 ユーザーのクエリに全く似ていない埋め込みを見つけたことを意味します。 私たちの場合は、ユーザーのクエリとソフトウェアエンジニアリングのチャンクの 間のコサイン類似性は0.983です。 これは、これら2つの埋め込みが非常に似ていることを意味します。なので、 これは、ソフトウェアエンジニアリングのテキストチャンクを取得し、それを ユーザーの質問のプロンプトに含めたいという合図です。さて、先に進む前に、 今すぐ少し混乱するかもしれませんが、後でベクトルデータベースを扱う際に 非常に役立つことが一つあります。 多くのベクトルデータベースのドキュメントでは、コサイン距離 と呼ばれるものを見かけるでしょう。これはコサイン類似性とは異なります。 それは1マイナスコサイン類似性として計算されます。 解釈しやすい数値を出すために、この調整がよく行われます。 コサイン距離では、ゼロに近い値は高い類似性を意味し、 それより大きい値は類似性が低いことを意味します。 これもベクトルデータベースのドキュメントで非常によく見かけるものです。 なので、コサイン距離とコサイン類似性の用語を見たら、それを覚えておいてください。 では、この数学を非常に高レベルで理解したので、軌道に戻りましょう。 ユーザーの質問との類似性が高いテキストチャンクを見つけたら、 ユーザーの質問を取得し、それをプロンプトに追加し、 そして見つけた最も関連性の高いテキストチャンクもプロンプトに含めます。 その後、そのプロンプトをClaudeに送信します。 それが、すべてのプロセスを詳細に説明したものです。 これで、最初から最後まで、背後にある技術や数学についても理解したので、 早速ノートブックで実装を始めましょう。 もうすぐです。
