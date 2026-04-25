# 49. BM25 lexical search

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287767
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
                                
                            
                        
                    
                
            
            
                
                
                
                    BM25 lexical search
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When building RAG pipelines, you'll quickly discover that semantic search alone doesn't always return the best results. Sometimes you need exact term matches that semantic search might miss. The solution is to combine semantic search with lexical search using a technique called BM25.

The Problem with Semantic Search Alone

Let's say you're searching for a specific incident ID like "INC-2023-Q4-011" in a document. While semantic search excels at understanding context and meaning, it might return sections that are semantically related but don't actually contain the exact term you're looking for.

In the example above, semantic search returned the cybersecurity section (which does contain the incident ID) but also returned a financial analysis section that doesn't mention the incident at all. This happens because semantic search focuses on conceptual similarity rather than exact term matching.

Hybrid Search Strategy

The solution is to run both semantic and lexical searches in parallel, then merge the results. This gives you the best of both worlds:

Semantic search finds conceptually related content using embeddings
Lexical search finds exact term matches using classic text search
Merged results combine both approaches for better accuracy

How BM25 Works

BM25 (Best Match 25) is a popular algorithm for lexical search in RAG systems. Here's how it processes a search query:

Step 1: Tokenize the query
Break the user's question into individual terms. For example, "a INC-2023-Q4-011" becomes ["a", "INC-2023-Q4-011"].

Step 2: Count term frequency
See how often each term appears across all your documents. Common words like "a" might appear 5 times, while specific terms like "INC-2023-Q4-011" might appear only once.

Step 3: Weight terms by importance
Terms that appear less frequently get higher importance scores. The word "a" gets low importance because it's common, while "INC-2023-Q4-011" gets high importance because it's rare.

Step 4: Find best matches
Return documents that contain more instances of the higher-weighted terms.

Implementing BM25 Search

Here's how to set up a basic BM25 search system:

# 1. Chunk your text by sections
chunks = chunk_by_section(text)

# 2. Create a BM25 store and add documents
store = BM25Index()
for chunk in chunks:
    store.add_document({"content": chunk})

# 3. Search the store
results = store.search("What happened with INC-2023-Q4-011?", 3)

# Print results
for doc, distance in results:
    print(distance, "\n", doc["content"][:200], "\n----\n")

When you run this search, you'll get much better results than semantic search alone. The BM25 algorithm prioritizes sections that actually contain your specific search terms, especially rare terms like incident IDs.

Notice how the results now properly prioritize the Software Engineering section and Cybersecurity section - both of which actually contain the incident ID you're searching for.

Why This Works Better

BM25 excels at finding exact matches because it:

Gives higher weight to rare, specific terms
Ignores common words that don't add search value
Focuses on term frequency rather than semantic meaning
Works especially well for technical terms, IDs, and specific phrases

The key insight is that both search methods have complementary strengths. Semantic search understands context and meaning, while lexical search ensures you don't miss exact term matches. By combining them, you create a more robust search system that handles both conceptual queries and specific lookups effectively.

In the next step, you'll learn how to merge results from both search systems to create a unified hybrid search experience.
                            
                        
                    

                    
                        
                            Downloa

---

## 🎬 Transcript (English)

We've got the first iteration of our RAG pipeline put together. Everything looks good right now, but we're going to very quickly realize that, well, maybe we are not getting the best search results. Let me show you an example. If you open up the report.md file and scroll down just a little bit to the software engineering section, here it is right here. You'll notice that it has the statement of INC, which is short for Incident, 2023 Q4-011. And it looks like that search term occurs three times inside of this paragraph. So here's one right here, two right there, three right here. And if I continue searching throughout the document, I'll see that it is also mentioned down here inside of Section 10, Cybersecurity Analysis. It's mentioned inside the header, and then one time inside the actual paragraph itself right there. Now, I want to try searching for this term, this incident 2023 Q4011. And we're just going to see what happens. In other words, what search results do we actually get back using semantic search? So back inside of my notebook, I'm going to update the user query right here to be what happened with incident 2023. Then I'm going to rerun all cells and we'll see what result we get. All right, so take a look at this. It's a little bit surprising result. We get section 10, which is good. That's definitely the result we would want to see at first, in the list, because section 10 is all about this incident. But then very surprisingly, the next result is section 3, financial analysis. Well, if you open up section 3, right here, you'll notice that nowhere inside of section 3 is that incident ever mentioned. So we are getting some output from our semantic search that is a little bit surprising here. What we really wanted to get back was section 10 and then section 2, but what we got was section 10 and then unfortunately section 3. And section 3 appears to be completely irrelevant when it comes to investigating this incident. So even though the semantic search technique we put together is really fantastic and it's going to work well a lot of the time, there are these corner cases where it really just doesn't quite work as expected. So let's take a look at a technique we can use to improve our search results and hopefully get the results we want, which is Section 10 and then Section 2. All right, so here's the general strategy we are going to use. Whenever a user asks a question, we're going to feed that question into our semantic search side of the equation, which is generating those embeddings and using the vector database. But then in parallel, at the same time, we're also going to implement a separate lexical search system. Now, lexical search is more like classic text search, where we are going to break down the user's question into individual words and then trying to find chunks of text that seem to include those words. Once we go through the search process in both different systems, we'll get two sets results and then we will merge the results together. And the hope here is that we'll get a little bit better balance of search results where we get both the kind of semantic aspect and the plain text search aspect included in one result set. So hopefully we will eventually get a result that looks like this over here. Now to implement this lexical search, there are a tremendous number of methods for implementing a text search, but a very common method that you're going to see used in RAG pipelines, like the one we are building right now, is a technique referred to as BM25. Now this is short for Best Match 25. In the rest of this video, I'm going to give you a high-level overview of how this algorithm works, and I'm going to take a look at a notebook that actually implements BM25, so we'll be able to play around with it directly and see what kind of search results we get. So here's the general idea behind the BM25 algorithm. Now, again, I'm going to give you a high-level overview, and I'm going to leave out a couple of smaller steps just to simplify things and make it easier to understand. Everything is going to begin with us receiving a user's query. And let's imagine this case, they put in a search string like this right here, just A, so the word A, and then incident 2023Q4011. In step one, we're going to tokenize the user's query. And that means we're going to break it up into separate chunks. There are different ways in which we can tokenize a user's query, but right now we're going to use a very simple method, which is to just remove punctuation and break up the return all terms based upon spaces. So in this case, I would end up with separate search query terms of A and an incident 2023. Next, we're going to see how often each of these different search terms occurs across all of our different documents, or in our case, really text chunks. So let's imagine that we only have two text chunks in this scenario. So we're going to see how often the word A, and the word incident, blah, blah, blah, occurs across each of these chunks. And it looks like this first chunk right here has A right there, A right there, and then the second one has A, A, A. So in total, I would count all those up and I would have five A's. And then I would see how often I have incident 2023. It looks like there's only one right here. So I'd end up with a frequency of one. Next up, we're going to assign a relative importance to each term based upon its usage frequency. So in the case of the word A, it was used five times. And because it was used rather often, we're going to say this term is not super important because it is used all the place across all of our different documents, or again, our case, our text chunks. But incident 2023, that was used very infrequently, which means it is probably going to be of greater search importance. Then finally, in the last step, we're going to find the text chunk that uses the higher weighted terms more often. So in this case, the first text chunk right here, it only has two A's, whereas the second one has three A's, but A's are not super important because they're used rather frequently across all over different chunks. However, Text Chunk 1 uses Incident 2023 one time, and that is a highly weighted term. It's a really important term. So in this case, we would say this is probably our best text chunk, and we would want to return this as a prime search result. Now again, to see all this in action, let's take a look at a quick Jupyter Notebook. So back inside of my editor, I'm going to find a new notebook. This one is called 004 underscore BM25. Again, at the top, I've got some code relating to a chunking by section. I've then got a basic implementation of BM25 in the form of this class called BM25index. So I'm going to collapse that cell, make sure I run it. I'm going to read the contents of our report file. And then we're going to go through three separate steps here. We're going to first chunk the text by section. We're going to create a BM25 index store. And we're going to add each text chunk to it. And then we're going to attempt to search the store. And once again, our hope here is that we're going to maybe get some search results that look a little bit closer to this. Maybe not exactly these results, but I definitely want to see the sections that use Incident 2023 before I ever see some results that don't include that search term at all. So let's see how we do. Okay, let's take care of step one here. We need to chunk the text by section. So we've gone over this a couple times now. We'll say chunks is chunk by section with text. Next up, I'm going to create a store. And I'm going to loop over all my chunks and add them in as documents to the store. So I'll say for chunk in chunks store add document. And I'll pass in a dictionary with a content of chunk. I'm gonna run that. And I'll finally, I'm going to search over the store. I'll say store search. And I'll use that same term that I used in the previous notebook that did not give us the very good result. So I'll ask what happened with incident 2023 Q4011. And I'm going to ask for the first three search results. And then I'm going to print up the results very nicely just so we can interpret them really well. We'll say for doc, distance in results. And I'll print out the distance, a new line, doc with content. And again, I'm only going to print out the first 200 lines. And then how about a new line, a couple of separators in another new line. I'm going to run this and we'll see what we get. All right, so that's a much better search result than what we had before. Now I'm going to see software engineering first and then cybersecurity after that and then methodology down here. So now I am actually prioritizing the sections that use the most important search term inside my query, which was the incident 2023. And you'll notice that I don't really have quite as much importance around the other terms like what happened with. Those aren't quite as important terms, and they might be used several times inside of the original report, so I would not weigh those as heavily in the output results. But this incident 2023, that's a very rare term inside of a report, so it should definitely have a much higher weighting. And we can see that reflected very clearly inside of our search results. All right, so now, at this point in time, we have two separate search systems. We have semantic search put together, and we have this kind of more lexical, a little bit more classic text search system. And you might notice that in the implementation of these two stores, Back up here in the cell right here, I put them together with a rather similar API. They both have a add document function and they both have a search function down here as well. So now that we have these two separate search systems, one which implements semantic search and one which implements lexical search, we're going to come back in the next video and we're going to merge these two search systems together. Whenever a user submits a query, we're going to forward it off to both of these different search systems. We're going to get back a set of results from both and we're going to merge those results together. And hopefully we'll have all the best outcomes of semantic search along with some of the more classic results of lexical search as well.

---

## 🎬 トランスクリプト（日本語）

RAGパイプラインの最初のイテレーションを 構築しました。現時点ではすべて順調ですが、 すぐに気づくことになるでしょう。それは、 おそらく最高の検索結果が得られていないということです。 例を見てみましょう。レポートの `report.md` ファイルを 開いて、少し下にスクロールして ソフトウェアエンジニアリングのセクションに行くと、 ここにあります。INC、つまりインシデントの略で、2023 Q4-011 という記述があります。 そして、この検索語は この段落内に3回出現しているようです。 ここが1つ目、2つ目が ここ、3つ目がここにあります。そして、 ドキュメント全体を検索し続けると、サイバーセキュリティ分析のセクション10にも 記載されていることがわかります。 ヘッダー内に記載があり、その後、実際の 段落内にも1回記載されています。さて、 この用語、このインシデント 2023 Q4011 を検索してみます。 そして、何が起こるか見てみましょう。つまり、 セマンティック検索を使用して、どのような検索結果が得られるでしょうか？ ノートブックに戻り、ユーザー クエリをインシデントに関する 2023年問題に更新します。 そして、すべてのセルを再度実行し、どのような結果が得られるか見てみましょう。 さて、これを見てください。少し 驚くべき結果です。セクション10が得られました。 これは良いことです。それは間違いなく 私たちが最初に期待する結果です。なぜなら、セクション 10 はすべてこのインシデントに関するものだからです。しかし、 非常に驚くべきことに、次の結果はセクション3、 財務分析です。さて、セクション3を開くと、 ここに、 セクション3のどこにも、 このインシデントが言及されていないことに気づくでしょう。したがって、 セマンティック検索から得られる出力には、 少し驚くべきものがあります。私たちが本当に得たかったのは セクション10、そして次にセクション2でした。 しかし、得られたのはセクション10、そして残念ながら セクション3でした。セクション3は、 このインシデントの調査に関して、完全に無関係であるように思われます。したがって、 構築したセマンティック検索技術は非常に優れていて、 多くの場合はうまく機能しますが、 期待通りに機能しないコーナーケースもあります。そこで、 検索結果を改善できるテクニックを見てみましょう。 そして、うまくいけば、目的の結果、つまりセクション10 とセクション2が得られるでしょう。さて、 ここで一般的な戦略を示します。ユーザーが質問をすると、 その質問を、 埋め込みを生成し、ベクトルデータベースを使用する セマンティック検索側に渡します。 しかし同時に、並行して、 別のレキシカル検索システムも実装します。 レキシカル検索は、より 古典的なテキスト検索に近く、ユーザーの質問を 個々の単語に分解し、 それらの単語が含まれていると思われるテキストチャンクを 見つけようとします。両方のシステムで検索プロセスを 行った後、2セットの結果が得られ、 それらの結果をマージします。 ここで期待するのは、検索結果のバランスが 少し良くなることです。セマンティックな側面と プレーンテキスト検索の側面の両方を 1つの結果セットで得られるようにすることです。 うまくいけば、最終的にこのような結果が得られるでしょう。 さて、このレキシカル検索を実装するために、 テキスト検索を実装するための方法は数多くありますが、 RAGパイプライン、特に現在構築中のようなもの でよく見られる一般的な方法は、 BM25 と呼ばれるテクニックです。 これは Best Match 25 の略です。 このビデオの残りの部分では、このアルゴリズムがどのように機能するかについて、 概要を説明します。そして、実際にBM25を実装する ノートブックを見ていきます。 それで直接操作して、どのような検索結果が得られるか見てみましょう。 BM25 アルゴリズムの一般的な考え方は次のとおりです。 再度、概要を説明し、簡略化して 理解しやすくするために、いくつかの小さなステップは省略します。 すべては、ユーザーからのクエリを受け取ることから始まります。 そして、この例を考えてみましょう。彼らはこのような検索文字列を入力しました。 すなわち、単語 A、そしてインシデント2023Q4011。 ステップ1では、ユーザーのクエリをトークン化します。 つまり、それを個別のチャンクに分割します。 ユーザーのクエリをトークン化する方法はいくつかありますが、 今回は非常に単純な方法を使用します。 それは句読点を削除し、 すべての単語をスペースで区切ることです。 この場合、別々の検索クエリ 用語として A とインシデント2023 が得られます。 次に、これらの各検索用語が、 すべてのドキュメント、または 今回の場合はテキストチャンクにどれだけ頻繁に出現するかを調べます。 そこで、このシナリオではテキストチャンクが2つしかないと仮定しましょう。 したがって、単語 A と単語 インシデント blah blah blah が各チャンクにどれだけ頻繁に出現するかを見ます。 そして、この最初のチャンクには A がここに、A がここにあります。 そして、2番目のチャンクには A、A、A があります。 合計すると、それらをすべて数えると、5つの A があります。そして、インシデント 2023 がどれだけ頻繁に出現するかを見ます。ここには1つだけあるようです。 なので、頻度は 1になります。次に、各用語の 相対的な重要度を、 出現頻度に基づいて割り当てます。したがって、単語 A の場合、 5回使用されました。そして、それはかなり頻繁に 使用されたため、この用語はあまり重要ではないと 言えます。なぜなら、すべてのドキュメント、または 今回の場合はテキストチャンク全体で使われているからです。しかし、インシデント2023は 非常にまれに出現したため、 検索の重要度が高いと予想されます。 次に、最後に、重み付けされた用語を より頻繁に使用するテキストチャンクを見つけます。 したがって、この場合、最初のテキストチャンクには A が2つありますが、2番目の チャンクには A が3つあります。しかし、A は あまり重要ではありません。なぜなら、すべての チャンクでかなり頻繁に使用されているからです。しかし、テキストチャンク1は インシデント2023 を1回使用しており、 それは重み付けが高く、非常に重要な用語です。 したがって、この場合、これが最良のテキストチャンクであり、 これを主要な検索結果として返したいでしょう。 さて、これをすべて実際に見るために、短いJupyter Notebookを見てみましょう。 エディタに戻り、 新しいノートブックを探します。これは004 アンダースコアBM25と呼ばれています。再び、 一番上には、セクションごとのチャンクに関するコードがあります。 次に、BM25 の基本的な実装が BM25index というクラスの形であります。 そのセルを折りたたんで、実行します。レポートファイルの 内容を読み込みます。そして、 ここでは3つの別々のステップを行います。まず テキストをセクションごとにチャンク化します。BM25インデックスを 作成します。 そして、各テキストチャンクをそれに 追加します。そして、ストアを検索します。そして再び、 ここでは、以前のノートブックで、結果が良くなかった 同じ用語を使用して、結果が少しでも 近づくことを期待しています。これらの結果と完全に同じではないかもしれませんが、 少なくとも、インシデント2023を使用するセクションが、 検索語が含まれていない結果を見る前に、 確実に確認したいです。 どのように機能するか見てみましょう。さて、ステップ1に進みましょう。テキストを セクションごとにチャンク化する必要があります。 これは数回説明しました。 チャンクはセクションごとに テキストをチャンク化すると言います。次に、 ストアを作成します。 そして、すべてのチャンクをループして、 ドキュメントとしてストアに追加します。 チャンクをループして、ストアに追加します。 ドキュメントを追加します。 コンテンツとしてチャンクを含む辞書を渡します。 それを実行します。そして最後に、ストアを検索します。 ストアを検索します。 そして、前のノートブックで、良い結果が得られなかった のと同じ用語を使用します。 それで、インシデント2023 Q4011 の 何が起こったか尋ねます。 そして、最初の3つの検索結果を要求します。 そして、結果を非常にきれいに印刷して、 解釈できるようにします。結果の 各ドキュメントと距離についてループします。 そして、距離と新しい行、 コンテンツを持つドキュメントを印刷します。 そして、最初の200行だけを印刷します。そして、 新しい行、いくつかの区切り文字、そして別の新しい行を追加します。 それを実行して、何が得られるか見てみましょう。 さて、これは以前よりもはるかに良い検索結果です。 まずソフトウェアエンジニアリング、次にサイバーセキュリティ、 そして方法論がここにあります。 だから、私は今、クエリ内の最も 重要な検索語であるインシデント2023を 使用しているセクションを実際に優先しています。 そして、ソフトウェアエンジニアリングとサイバーセキュリティ、 そして方法論です。 私は今、クエリ内の最も重要な検索語を使用しているセクションを 実際に優先しています。それはインシデント2023でした。 そして、他の単語 例えば「何が起こったか」のようなものに対する 重要性はあまりありません。それらは、 元のレポート内で数回使用されている可能性があり、 そのため、結果での重み付けはそれほど高くしません。しかし、インシデント2023、 それはレポート内で非常にまれな用語なので、 間違いなく、より高い重み付けを持つべきです。 そして、それが検索結果に非常によく反映されているのがわかります。 さて、現時点で、2つの別々の検索システムがあります。 セマンティック検索システムと、 この種のよりレキシカルな、より古典的な テキスト検索システムがあります。そして、これらの2つのストアの実装で 気づくかもしれませんが、ここ、このセルで、 比較的似たAPIでそれらをまとめました。 どちらもドキュメント追加関数と、 ここにも検索関数があります。したがって、 これらの2つの別々の検索システム、つまり セマンティック検索を実装するものと、 レキシカル検索を実装するものを備えたので、 次のビデオに戻り、 これらの2つの検索システムを統合します。 ユーザーがクエリを送信すると、それを 両方の検索システムに転送します。両方から結果のセットを取得し、 それらの結果をマージします。そしてうまくいけば、 セマンティック検索のすべての優れた結果と、 レキシカル検索の古典的な結果の一部も 得られるでしょう。
