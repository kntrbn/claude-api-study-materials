# 45. Text chunking strategies

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287776
**Section:** 07 RAG and Agentic Search

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    2
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Text chunking strategies
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Text chunking is one of the most critical steps in building a RAG (Retrieval Augmented Generation) pipeline. How you break up your documents directly impacts the quality of your entire system. A poor chunking strategy can lead to irrelevant context being inserted into your prompts, causing your AI to give completely wrong answers.

Consider this example: you have a document with sections on medical research and software engineering. If you chunk poorly, a user asking "How many bugs did engineers fix this year?" might get information about medical research instead of software engineering, simply because the medical section happened to contain the word "bug" in a different context.

This is why choosing the right chunking strategy matters so much. Let's explore three main approaches.

Size-Based Chunking

Size-based chunking is the simplest approach - you divide your text into strings of equal length. If you have a 325-character document, you might split it into three chunks of roughly 108 characters each.

This method is easy to implement and works with any type of document, but it has clear downsides:

Words get cut off mid-sentence
Chunks lose important context from surrounding text
Section headers might be separated from their content

To address these issues, you can add overlap between chunks. This means each chunk includes some characters from the neighboring chunks, providing better context and ensuring complete words and sentences.

Here's a basic implementation:

def chunk_by_char(text, chunk_size=150, chunk_overlap=20):
    chunks = []
    start_idx = 0
    
    while start_idx < len(text):
        end_idx = min(start_idx + chunk_size, len(text))
        chunk_text = text[start_idx:end_idx]
        chunks.append(chunk_text)
        
        start_idx = (
            end_idx - chunk_overlap if end_idx < len(text) else len(text)
        )
    
    return chunks

Structure-Based Chunking

Structure-based chunking divides text based on the document's natural structure - headers, paragraphs, and sections. This works great when you have well-formatted documents like Markdown files.

For a Markdown document, you can split on header markers:

def chunk_by_section(document_text):
    pattern = r"\n## "
    return re.split(pattern, document_text)

This approach gives you the cleanest, most meaningful chunks because each one represents a complete section. However, it only works when you have guarantees about your document structure. Many real-world documents are plain text or PDFs without clear structural markers.

Semantic-Based Chunking

Semantic-based chunking is the most sophisticated approach. You divide text into sentences, then use natural language processing to determine how related consecutive sentences are. You build chunks from groups of related sentences.

This method is computationally expensive but produces the most relevant chunks. It requires understanding the meaning of individual sentences and is more complex to implement than the other strategies.

Sentence-Based Chunking

A practical middle ground is chunking by sentences. You split the text into individual sentences using regular expressions, then group them into chunks with optional overlap:

def chunk_by_sentence(text, max_sentences_per_chunk=5, overlap_sentences=1):
    sentences = re.split(r"(?<=[.!?])\s+", text)
    
    chunks = []
    start_idx = 0
    
    while start_idx < len(sentences):
        end_idx = min(start_idx + max_sentences_per_chunk, len(sentences))
        current_chunk = sentences[start_idx:end_idx]
        chunks.append(" ".join(current_chunk))
        
        start_idx += max_sentences_per_chunk - overlap_sentences
        
        if start_idx < 0:
            start_idx = 0
    
    return chunks

Choosing Your Strategy

Your choice depen

---

## 🎬 Transcript (English)

Inside of this video and the next couple of videos, we're going to start to implement our own custom rag workflow inside of a series of different notebooks. We're going to first focus on just making the most simple basic rag setup we can possibly make, and then we're going to add in some additional steps over time. Now, as a reminder, A typical rag pipeline looks a little bit like this to really simplify things. We're going to take a source document, break it up into chunks of text, then whenever user asks us a question, we're going to find some relevant chunk of text, put it into a prompt, and that's pretty much the entire thing. So step one of this entire flow is to take a source document and break it up into chunks of text. Now believe it or not, this process of taking a document and breaking it up into separate chunks is one of the more complex steps of the entire rag pipeline. Simply because how we chunk our document up has a huge output on the quality of our rag pipeline. And I want to give you an example right away to help you understand why that's the case. So take a look at this source document. It's just a couple of little lines, and it's supposed to represent some kind of report from a company or something like that. And just reading through it really quickly, we can see that there's really three general areas. We have a header, we have a section about medical research, and then a section about software engineering. Now there are many ways in which we could divide this thing up into separate chunks, but I'm just going to suggest one way. I'm going to say for every kind of distinct line inside this document, we're going to make a separate chunk. So we'd end up with about five separate chunks like the ones you see right here. If you consider each of these different chunks now, you will notice something really interesting. The third chunk of text right here is all about medical research. That's what this text is about. It was inside of the medical research section. But it contains the word bug. So at kind of a high level, if you just glanced at this paragraph alone, it is almost like it's kind of about software engineering, just because it contains the word bug. And then likewise, down here, we have the software engineering section, and inside of it is the word infection vectors. Infection vectors is a little bit more of a medical term. So once again, we have a section that is about software engineering, but the language inside of it is kind of about medical research. So now we want you to think about what would happen if we took these chugs and we added them into our rag pipeline. Let's imagine that a user asked a question of something like, how many bugs did engineers fix this year? So now our job as a part of the rag pipeline would be to find the chunks of text we have that are most relevant for the user's question. Well, the user said something about bugs. So, well, at first glance, this chunk of text right here seems relevant, just because it contains the word bug. So we might decide to take this chunk of text and add it as context into the overall prompt. And as you can tell right away, this is a huge error. The user wants to understand something about software engineering from the report. So we definitely wanted this section, but we erroneously got something about medical research instead. So this is an example where a chunking strategy can easily introduce huge errors and very bad context inserts into your prompt. So to solve this problem, we're going to spend a lot of time thinking about how we're going to take our original source document and break it up into different chunks of text. In this video, we're going to cover three different chunking strategies or methods to divide our document into separate chunks of text, each of which have some feature or some technique meant to address the problem that we just saw. So we are going to discuss size-based chunking, structure-based, and semantic-based. The first one we're going to cover is size-based chunking. This is where we take our big old document, so a big chunk of text, and we just divide it into a number of strings of equal length. This is by far the easiest technique to implement, and in some, also probably the one you're going to see most often in production implementations. So let's take a look at how size-based chunking is done. With size-based chunking, we're going to take our original document and divide it into some number of strings of more or less equal length. In our particular case, we have a source document with about 325 characters. So we could decide just completely arbitrarily to divide that into three separate chunks. And that means each chunk would have about 108 characters or so. So we might take the first 108 characters, put them into chunk 1, the next 108 put them into chunk 2, and just repeat for the entire document. Now, very simple technique, but right away it has a big downside. And that is that each chunk is probably going to end up with some number of cutoff words inside of it. You can see right away the first chunk has the word significant cutoff. So it's just significant key. in the first chunk and then ends the word in the next one. In addition, each chunk ends up lacking context. So for example, the third chunk down here unfortunately does not really include the section header that was right above it. And this section header would have provided a lot of context on what this text right here is really talking about. So to solve this problem that starts to come up right away if you use size-based chunking, we can implement a overlap strategy. An overlap strategy is where we are still going to do size-based chunking, but we're also going to include a little bit of overlap from the neighboring chunks. So for example, we have the original chunk one right here, but we might decide to include just a number of characters from the next chunk down. So in this case, we might include the rest of the word significant plus the end of that entire sentence. So we would end up with a chunk that looks like this that just has a little bit more meaning to it. And then for chunk 2, we would still have the body be this area right here, but we'd include an overlap of some number of characters from before the chunk and after the chunk. So with the strategy, we are going to end up with a decent amount of duplicated text. For example, in this case, we have section 1 medical research inside the second chunk, and that was also included inside the first one as well. So there is duplication of text, but the upside here is that each chunk of text has, in general, a little bit more context provided for it. The next kind of strategy that you're going to see is structure-based chunking. This is where we are going to divide off the text based upon the overall structure of our document. So we might try to find headers or paragraphs or general sections and use those as our dividing lines for each chunk. Implementing this strategy of chunking with our document would be really easy because our document is written with markdown syntax. We know that because it has a little pounds right here, the double hashes for each section. So we might look for these little pound symbols, and then say that every time we see this kind of symbol, that means we must be starting a brand new section. So we could very easily write out some code to programmatically split on the double hash characters. And we would end up with some pretty well-formed sections, like what you see right here. Now this might sound like a fantastic strategy, but unfortunately, reality just doesn't favor it quite so often. In many cases, you are going to be trying to ingest documents that are not formatted with Markdown syntax at all. They might be plain PDF documents that just contain plain text, in which case you will not get these very clearly delineated sections. So again, even though this seems like a great technique, implementing it can be really challenging, especially if you do not have any guarantees around the structure of your different documents. The last chunking strategy that we are going to discuss is semantic-based chunking. This is where you might take all of your text, divide it up into sentences or sections, and then use some kind of natural language processing technique to figure out how related each consecutive sentence is. you'll then build up your chunks out of groups of these somehow related sentences or sections. Now, as you can tell just by the description, this is by far definitely more advanced technique, so we're not going to look too closely into the actual implementation. The only reason I mention it at all is just to make it clear that there's really no set finite fixed number of chunking strategies. There's really an infinite number of ways in which we can decide to divide up our text. And so deciding upon which method you use really comes down to your particular use case and what guarantees you have around the documents that you are trying to ingest. Now before we move on, I want to go over a very quick example with you. So I've got a Jupyter notebook put together with three different chunking strategies implemented inside of it. So I would encourage you to find a notebook called 001 chunking. Also make sure that you download the accompanying report.md file and place it inside the same directory as that notebook. This report.md file has a little sample kind of fictional report inside of it that we're going to use for testing purposes as we learn about how to implement a rag pipeline. So inside of here, you'll find a couple of different cells. The first one contains a sample implementation of a chunk by character. So this is an implementation based upon the size-based strategy, where we are going to divide up our text into strings of equal length that also have some amount of overlap on them. You'll notice that the arguments are going to be the text, the size of each chunk, and then some amount of chunk overlap. So again, that is the number of characters we want to have on either side of the chunk. The next cell shows how we might chunk by sentence. So very similar idea, but now I'm using a regular expression to split the text up into individual sentences, and then each chunk will be formed out of some number of sentences with optionally a little bit of overlap on each side. And then finally, if we have really strong guarantees around the structure of our document and its exact contents, we might try to use a chunk by section, which would be an example of structure-based chunking. So in this example, it's going to look for a new line character, and then two pound signs, and then a space. And that is going to be our separation criteria. So we would get kind of executive summary would be the first chunk. Well, technically the second one, this would be the first chunk up here. But then we would get everything inside the executive summary all the way down to the table of contents that would start off our second chunk. And then the next chunk would be the methodology and then section one and so on. This will give us the best formatting for each chunk, because each chunk will consist of exactly one section, but it really only works because we have a guarantee around the structure of the document. We know it is marked down, and we know that we're only going to see that new line, pound, pound space, in the case that we have a new section beginning. Now let's test each of these really quickly. So back inside my notebook, I'm going to go down to the bottom cell and I'm going to first try out the chunk by character. So I'm opening up the file, getting all the text out of it. I'm going to chunk by character and then just print out each chunk with a little separator between each one. So I'll run that. and I will see that we get our first chunk right here, second, and so on. And right away, you can see that the default settings do not produce very good chunks. So the default settings are a chunk length of 150 with a overlap of 20. So in this case, each chunk doesn't really provide a whole lot of meaning. Like, what does this sentence right here really do for us? And can we really use it to answer any user question? I don't know, maybe not. So we might decide to dramatically change our default settings here. Maybe I want a chunk length of 500 with a overlap of 150. Let's see if that gives us something a little bit better. Okay, that's a little bit better than what we had before. So now I can start to see the formation of actual individual sections here that give us a little bit of information. You'll also very quickly start to notice the overlaps. So I can see addressing complex challenges. Let turns out that exact phrase is included inside of the chunk right above. So that's an example of the overlapping that we get. All right, next up, let's try our second strategy, which is chunk by sentence. And again, I'm going to use the default arguments. And this one actually looks like it's pretty strong. So this should give us five sentences by default in each chunk with one sentence of overlap. And we are using a regular expression to split up each sentence. So there might be cases where it doesn't split a sentence correctly. But at first glance, yeah, I'd say this looks pretty good. Each chunk appears to give us a solid amount of information. And then finally, we can try out chunk by section. Now run that. And now we can see that the first chunk is not going to contain a lot of useful information, but everything after that is really, really strong because we are getting exactly a single section each time. I get just the executive summary, and then the table of contents, and then section one, section two, section three, and so on. So once again, which strategy you use entirely comes down to the nature of your document and what guarantees you have around its structure. For us, chunk by section looks fantastic. But if we are expecting to receive user-provided documents where there are no guarantees around the formatting of each document, then using chunk by section is probably not going to work out in the long run. In that case, we might fall back to chunk by sentence. But even this might not work pretty well, work out pretty well. Imagine that we are trying to chunk user-provided code, for example. Well, if we try to split code up into individual sentences, we are probably going to get a lot of unexpected results, because code tends to have periods in very unexpected places. So that might mean that we just fall back to the old reliable standard, which is chunk by character. Chunk by character is not guaranteed to give you the best results, but it's going to work vast majority of the time and it's going to work out reasonably well.

---

## 🎬 トランスクリプト（日本語）

この動画と次のいくつかの動画で、私たちは 独自のカスタムRAGワークフローを実装し始めます。 複数の異なるノートブックに。まず 可能な限り最もシンプルで基本的なRAGのセットアップに 焦点を当てます。その後、時間の経過とともに追加の ステップを追加していきます。さて、おさらいですが、典型的な RAGパイプラインは、非常に単純化すると、このようになります。 ソースドキュメントを取り出し、テキストのチャンクに分割します。 ユーザーが質問をすると、関連するテキストのチャンクを見つけて プロンプトに入力します。ほぼそれがすべてです。 つまり、このフロー全体の手順1は、ソースドキュメントを取り出し テキストのチャンクに分割することです。信じられないかもしれませんが このドキュメントを取り出してチャンクに分割するプロセスは RAGパイプライン全体の中で最も複雑なステップの1つです。 なぜなら、ドキュメントをどのようにチャンクに分割するかが RAGパイプラインの品質に大きな影響を与えるからです。 その理由を理解していただくために、すぐに例を挙げたいと思います。 このソースドキュメントを見てください。ほんの数行です。 企業からのレポートのようなものを表すものです。そして それをざっと読むと、大きく分けて3つの領域があることがわかります。 ヘッダー、医学研究に関するセクション 、そしてソフトウェアエンジニアリングに関するセクションがあります。 このものをチャンクに分割する方法はたくさんありますが、 ここでは1つの方法を提案します。 このドキュメント内のすべての明確な行に対して 個別のチャンクを作成することにします。そうすると、約5つの個別の チャンクが得られることになります。これらの各チャンクを 見ると、非常に興味深いことに気づくでしょう。 3番目のテキストチャンクは、すべて医学研究に関するものです。 これは医学研究のセクションにあったものですが、 「バグ」という言葉が含まれています。したがって、大まかに言えば、 この段落だけをちらっと見ると、 「バグ」という言葉が含まれているために、 ソフトウェアエンジニアリングに関するもののように思えます。 同様に、ここではソフトウェアエンジニアリングのセクションがあり、 その中に「感染経路」という言葉があります。「感染経路」は やや医学的な用語です。したがって、 ソフトウェアエンジニアリングに関するセクションでありながら、 その中の言語は医学研究に関するもののように見えます。 では、これらのチャンクをRAGパイプラインに追加するとどうなるか考えてみましょう。 ユーザーが「エンジニアは今年何個のバグを修正しましたか？」のような質問を したと想像してください。 RAGパイプラインの一部としての私たちの仕事は ユーザーの質問に最も関連性の高いテキストのチャンクを見つけることです。 ユーザーはバグについて言及しました。ですから、 このテキストのチャンクが関連しているように見えます。 なぜなら、バグという言葉が含まれているからです。 そこで、このテキストチャンクを全体のプロンプトのコンテキストとして 追加することにするかもしれません。 そして、すぐにわかるように、これは重大な間違いです。 ユーザーはレポートからソフトウェアエンジニアリングについて何かを理解したいのです。 ですから、このセクションは絶対に必要でしたが、 代わりに医学研究に関するものを誤って取得しました。 したがって、これはチャンク化戦略が 簡単にプロンプトに重大なエラーと非常に悪いコンテキスト挿入を 引き起こす可能性のある例です。 この問題を解決するために、 元のソースドキュメントをどのように取り出し、 異なるテキストのチャンクに分割するかについて 多くの時間を費やすことにします。 この動画では、3つの異なるチャンク化戦略または 方法について説明します。これらはドキュメントを 個別のテキストチャンクに分割するためのもので、 それぞれが、先ほど見た問題に対処するための機能またはテクニックを備えています。 サイズベースのチャンク化、構造ベースのチャンク化、 セマンティックベースのチャンク化について説明します。 最初に説明するのはサイズベースのチャンク化です。 これは、大きなドキュメント、つまり大きなテキストのチャンクを取り出し、 それを同じ長さの文字列の数に分割するものです。 これは、実装が最も簡単な手法であり、 おそらく本番実装で最もよく見かけるものでしょう。 では、サイズベースのチャンク化がどのように行われるか見てみましょう。 サイズベースのチャンク化では、元のドキュメントを取り出し ほぼ同じ長さの文字列の数に分割します。 この場合、ソースドキュメントには約325文字があります。 したがって、完全に任意に、それを3つの個別のチャンクに分割することにしました。 つまり、各チャンクは約108文字になります。 最初の108文字を取り出し、チャンク1に入力し、次の108文字をチャンク2に 入力して、ドキュメント全体を繰り返します。 これは非常に単純な手法ですが、すぐに大きな欠点があります。 それは、各チャンクに切り取られた単語が いくつか含まれる可能性が高いということです。 最初のチャンクには「significant」という単語が 含まれており、「significant」の後に「key」が続き、 次のチャンクでその単語が終わります。 さらに、各チャンクはコンテキストを欠いています。 例えば、3番目のチャンクには 残念ながら、そのすぐ上にあるセクションヘッダーが含まれていません。 そして、このセクションヘッダーは、このテキストが何について話しているのかについて 多くのコンテキストを提供したでしょう。 したがって、サイズベースのチャンク化を使用した場合にすぐに発生する この問題に対処するために、 オーバーラップ戦略を実装できます。 オーバーラップ戦略とは、サイズベースのチャンク化を依然として行いますが、 隣接するチャンクから少しオーバーラップを含めることも します。例えば、ここにある元のチャンク1に 対して、次のチャンクからいくつかの文字を含めることにしました。 つまり、単語「significant」の残り部分と その文全体のエンド部分を含めるかもしれません。 したがって、より多くの意味を持つようなチャンクが得られます。 そして、チャンク2に対しては、 ここの領域を本体として保持しますが、 チャンクの前と後のいくつかの文字のオーバーラップを含めます。 したがって、この戦略では、かなりの量の重複したテキストが得られます。 例えば、この場合、チャンク2には「セクション1 医学研究」が含まれており、 これは最初のチャンクにも含まれていました。 したがって、テキストの重複はありますが、 ここでは、各テキストチャンクに、一般的に、 もう少しコンテキストが提供されるという利点があります。 次に、構造ベースのチャンク化という戦略を見ます。 これは、ドキュメント全体の構造に基づいて テキストを分割する方法です。 ヘッダー、段落、または一般的なセクションを見つけ、 それらを各チャンクの分割線として使用することを検討します。 このチャンク化戦略を私たちのドキュメントで実装することは 非常に簡単です。なぜなら、私たちのドキュメントは Markdown構文で書かれており、それは二重ハッシュ記号 が各セクションにあることでわかります。 ですから、これらの小さなハッシュ記号を探し、 この種の記号を見るたびに、新しいセクションが始まることを意味すると言えます。 したがって、二重ハッシュ文字でプログラム的に分割するコードを 簡単に記述でき、ここに示すような 非常に適切にフォーマットされたセクションが得られます。 これは素晴らしい戦略のように聞こえるかもしれませんが、残念ながら 現実はそれほど favourableではありません。 多くの場合、Markdown構文でフォーマットされていないドキュメントを 取り込もうとします。それらは プレーンなPDFドキュメントである可能性があり、 プレーンテキストのみが含まれている場合、 このように明確に区切られたセクションは得られません。 したがって、この技術は素晴らしいように思えますが、 実装は非常に困難になる可能性があります。 特に、ドキュメントの構造に関する保証がない場合。 最後に説明するチャンク化戦略は、セマンティックベースのチャンク化です。 これは、すべてのテキストを取り出し、 文またはセクションに分割し、 自然言語処理技術を使用して、 連続する各文がどの程度関連しているかを把握します。 次に、関連する文またはセクションのグループから チャンクを構築します。 説明からわかるように、これははるかに高度なテクニックなので、 実際の実装を詳しく見ていくことはしません。 私がそれを言及する唯一の理由は、 チャンク化戦略に設定された固定の有限の数がないことを 明確にするためです。 テキストを分割する方法は無限にあります。 したがって、どの方法を選択するかは、 特定のユースケースと、取り込もうとしている ドキュメントに関する保証に依存します。 次に進む前に、非常に簡単な例を説明します。 そこで、3つの異なるチャンク化戦略を実装した Jupyterノートブックを用意しました。 なので、001チャンクというノートブックを見つけて、 関連するreport.mdファイルもダウンロードして、 そのノートブックと同じディレクトリに配置してください。 このreport.mdファイルには、テスト目的で使用する 簡単な架空のレポートが含まれています。 RAGパイプラインの実装方法を学ぶ際に。 なので、ここにはいくつかの異なるセルがあります。 最初のセルには、文字ごとのチャンクのサンプル実装が含まれています。 これはサイズベースの戦略に基づいた実装で、 テキストを同じ長さの文字列に分割し、 さらにそれらの上にオーバーラップを含めます。 引数はテキスト、各チャンクのサイズ、 そしてチャンクのオーバーラップ量になります。 したがって、それらはチャンクの両側にある文字数です。 次のセルは、文ごとのチャンク方法を示しています。 考え方は非常に似ていますが、 今回は正規表現を使用してテキストを個々の文に分割し、 各チャンクは、オプションで両側に少しオーバーラップを持つ いくつかの文で構成されます。 そして最後に、ドキュメントの構造とその正確なコンテンツに関する 非常に強力な保証がある場合、セクションごとのチャンクを 使用することを検討します。これは構造ベースのチャンク化の例です。 したがって、この例では、改行文字、 2つのハッシュ記号、そしてスペースを探します。 それが区切り基準になります。 だから、エグゼクティブサマリーが 最初のチャンクになるでしょう。まあ、技術的には2番目のものですが、 これが最初のチャンクになります。しかし、その後、 目次まで、エグゼクティブサマリー内のすべてのものが 2番目のチャンクを開始することになります。 そして、次のチャンクは方法論、その後セクション1、セクション 2、セクション3となります。 これは、各チャンクが正確に1つのセクションで構成されるため、 各チャンクに最適なフォーマットを提供します。 しかし、それはドキュメントの構造に関する保証がある場合にのみ機能します。 私たちはそれがMarkdownであり、 新しいセクションが始まる場合にのみ 改行、ハッシュ、ハッシュ、スペースが見られることを知っています。 では、これらを実際にテストしてみましょう。 ノートブックに戻り、最後のセルに移動します。 まず、文字ごとのチャンクを試してみます。 ファイルを開き、すべてのテキストを取得します。 文字ごとにチャンク化し、各チャンクを 小さな区切り文字で出力します。 それを実行します。そして、最初のチャンクがここにあり、 2番目、そしてそれ以降が得られることがわかります。 そしてすぐに、デフォルト設定では あまり良いチャンクが生成されないことがわかります。 デフォルト設定はチャンク長150、オーバーラップ20です。 したがって、この場合、各チャンクは あまり意味のある情報を提供していません。たとえば、この文は何でしょうか？ そして、ユーザーの質問に答えるためにこれを使用できるでしょうか？ わかりません、おそらくできません。 そこで、デフォルト設定を大幅に変更することにしました。 たとえば、チャンク長を500、 オーバーラップを150にしたいとします。 それがもう少し良くなるかどうか見てみましょう。 はい、以前よりはましです。 これで、実際の個々のセクションの形成が見え始めます。 少し情報を提供しています。 オーバーラップもすぐに気づき始めるでしょう。 例えば、「複雑な課題に取り組む」というフレーズが すぐ上のチャンクに含まれていることがわかります。 だから、それは私たちが得るオーバーラップの例です。 さて、次に、2番目の戦略、 文ごとのチャンクを試してみましょう。 再び、デフォルトの引数を使用します。 そして、これはかなり強力に見えます。 デフォルトでは各チャンクに5つの文が含まれ、 1つの文のオーバーラップがあります。 各文を分割するために正規表現を使用しています。 したがって、文を正しく分割できない場合があるかもしれません。 しかし、一見したところ、これはかなり良いですね。 各チャンクは、かなりの量の情報を提供しているようです。 そして最後に、セクションごとのチャンクを試すことができます。 それを実行します。 そして今、最初のチャンクには あまり有用な情報は含まれませんが、 それ以降はすべて非常に強力です。 なぜなら、各チャンクが正確に1つのセクションであるからです。 エグゼクティブサマリーだけを取得し、 次に目次、次にセクション1、セクション 2、セクション3となります。 したがって、繰り返しになりますが、 どの戦略を使用するかは、 ドキュメントの性質と その構造に関する保証に完全に依存します。 私たちにとっては、セクションごとのチャンクは素晴らしいですが、 ユーザー提供のドキュメントを受け取ることを期待しており、 各ドキュメントのフォーマットに関する保証がない場合、 セクションごとのチャンクを使用するのは、 おそらく長期的にはうまくいかないでしょう。 その場合、文ごとのチャンクにフォールバックするかもしれません。 しかし、これもそれほどうまくいかないかもしれません。 例えば、ユーザー提供のコードをチャンク化しようとしていると想像してください。 コードを個々の文に分割しようとすると、 予期しない結果が多く得られるでしょう。 なぜなら、コードは非常に予期しない場所に ピリオドを持つ傾向があるからです。 つまり、昔ながらの信頼できる標準、 つまり文字ごとのチャンクにフォールバックする必要があるかもしれません。 文字ごとのチャンクは最高のとは限りませんが、 大多数の場合うまくいき、 reasonably well に機能します。
