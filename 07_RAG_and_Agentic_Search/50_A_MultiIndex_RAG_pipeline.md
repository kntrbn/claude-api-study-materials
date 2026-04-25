# 50. A Multi-Index RAG pipeline

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287766
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
                                
                            
                        
                    
                
            
            
                
                
                
                    A Multi-Index RAG pipeline
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                We've built separate implementations for semantic search (using vector embeddings) and lexical search (using BM25). Now it's time to combine them into a unified search pipeline that leverages the strengths of both approaches.

The Multi-Index Architecture

Both our VectorIndex and BM25Index classes share nearly identical APIs - they both have add_document() and search() methods. This consistency makes it straightforward to wrap them together in a new class called Retriever.

The Retriever acts as a coordinator that forwards user queries to both indexes, collects their results, and merges them using a technique called reciprocal rank fusion.

Understanding Reciprocal Rank Fusion

Merging results from different search methods isn't as simple as just concatenating lists. Each method uses different scoring systems, so we need a way to normalize and combine their rankings fairly.

Here's how reciprocal rank fusion works with an example. Let's say we search for information about "INC-2023-Q4-011" and get these results:

VectorIndex returns: Section 2 (rank 1), Section 7 (rank 2), Section 6 (rank 3)
BM25Index returns: Section 6 (rank 1), Section 2 (rank 2), Section 7 (rank 3)

We combine these into a single table showing each text chunk's rank from both indexes, then apply the RRF formula:

RRF_score(d) = Σ(1 / (k + rank_i(d)))

Where k is a constant (often 60, but we'll use 1 for clearer results) and rank_i(d) is the rank of document d in the i-th ranking.

For our example:

Section 2: 1.0/(1+1) + 1.0/(1+2) = 0.833
Section 7: 1.0/(1+2) + 1.0/(1+3) = 0.583
Section 6: 1.0/(1+3) + 1.0/(1+1) = 0.75

The final ranking becomes: Section 2 (0.833), Section 6 (0.75), Section 7 (0.583). This makes intuitive sense - Section 2 performed well in both indexes, so it rises to the top.

Implementation Details

The Retriever class wraps multiple search indexes and provides a unified interface:

class Retriever:
    def __init__(self, *indexes: SearchIndex):
        if len(indexes) == 0:
            raise ValueError("At least one index must be provided")
        self._indexes = list(indexes)
    
    def add_document(self, document: Dict[str, Any]):
        for index in self._indexes:
            index.add_document(document)
    
    def search(self, query_text: str, k: int = 1, k_rrf: int = 60):
        # Get results from all indexes
        all_results = []
        for idx, results in enumerate(all_results):
            for rank, (doc, _) in enumerate(results):
                # Track document ranks across indexes
                # Apply RRF scoring formula
        # Return merged and sorted results

The key insight is that by maintaining consistent APIs across different search implementations, we can easily combine them without tight coupling.

Testing the Hybrid Approach

Remember our earlier problem where searching for "what happened with INC-2023-Q4-011?" returned unexpected results from the vector-only approach? The cybersecurity incident (Section 10) came first, but financial analysis (Section 3) came second instead of the more relevant software engineering section.

With our hybrid retriever, we now get much better results:

Section 10: Cybersecurity Analysis - Incident Response Report (most relevant)
Section 2: Software Engineering - Project Phoenix Stability Enhancements (second most relevant)
Section 5: Legal Developments (third)

This demonstrates how combining semantic and lexical search can overcome the limitations of either approach used alone.

Extensibility

The beauty of this architecture is its extensibility. Since all indexes implement the same SearchIndex protocol with add_document() and search() methods, you can easily add new search methodologies:

Want to add a keyword-based index? A graph-based search? A specialized domain index? 

---

## 🎬 Transcript (English)

We now have an implementation for semantics search and an implementation for lexical search. So now we need to wire these things up together. Let me show you how we're going to do that. The first thing to notice is that the implementation for both these searching functionalities have the almost exact same public API. So we have a vector index class on the left hand side that has methods like add document and search, and we have almost identical methods inside of our BM25 index as well. So to connect these two things together into a single search pipeline, we're going to wrap them up inside of a new class that we will call retriever. This retriever is going to receive a user's question and then forward it on to the search methods of vector index and BM25 index. The retriever will then receive the results from both them and figure out some way of actually merging the results together. Now it turns out that the merge operation is actually a little bit tricky. So I want to go into all bit of detail on how you can merge results that are coming out of these different search methodologies. To combine the results together, we're going to use a technique known as reciprocal rank fusion. The easiest way to understand this technique is to go through an example. So let's do that right now. Let's imagine that we run a search on the vector index and we get outputs of section 27 and then 6. And then we do the same exact search on BM25 and we get 6, 2, and 7. So now we need to take these two list of results and combine them together in some way. To do so, I'm going to take all the search results and put them together on a single table, like so. So now I've got text chunk 27 and 6 and I've recorded the rank from the vector index output and the rank from the BM25 index output. And to be clear, when I'm talking about rank, I just mean kind of search output position. So rank 1, 2, 3, rank 1, 2, 3, I'm just kind of putting those same exact numbers on this chart down here. Once I have all those ranks in place, I'm then going to apply a formula. Here's the exact formula right here, and I know it looks really terrible, but don't worry, it's not as complicated as it looks. Here's how it works. For every rank column we have, so like that column right there and that column right there, we're going to write out a separate term. So here's the term for the first column, here's the term for the second column. In the first term, we're going to write out 1 over 1 plus whatever number is right there. So we end up with 1 over 1 plus 1. And then the second term will be 1 over 1 plus whatever number is right there. So 1 over 1 plus 2. Once we have calculated the score for each text chunk, we're then going to sort the table based upon score from greatest to least. So we're going to end up with something like this. So we'd end up with text chunk for section 2 as being the most relevant search result. Section 6 would be the second most and section 7 would be the least relevant. And this kind of makes sense. We can kind of visually confirm that these outputs make sense if you just look at the individual rank outputs from each search methodology. So section 2 was rank 1 and 2. That means, hey, in general, it's trending up towards the top. Section 6 is 1 and 3. That's kind of like in the middle. It has a good score in a bad score. And then section 7 is 2 and 3. And so it trends down towards the bottom. So with a visual inspection, the results, I think, do make a decent amount of sense. All right. So now that we understand how we're going to combine the results together, let's go back over to our Jupyter notebook. And we're going to take a look at a sample implementation of a retriever class and a sample implementation of merging the results. Okay, so back over here, I move on to the next notebook, which is 005 hybrid. Once again, there's a lot of setup up here. So I've got the vector database implementation, the VM25 implementation, and now I've added in a implementation for the retriever class as well. The retriever has method of add document. And if you call add document, it's just going to take whatever document you pass in and pass it off to each of the different indexes that are contained inside the retriever. So in our case, our indexes are the vector index and the BM25 index. Then the retriever also has a search function. If you pass in some query text to it, that query text will be passed off to each of the different indexes that are contained inside the retriever. We then take all the results that come back and combine them together. So here is the merge logic that implements that reciprocal rank fusion. All right, so time to do a little test here. Now, I want you to recall what led us down this entire path was back on our vector database implementation. So this notebook over here, we found that if we search for something like what happened with incident 2023, we got back some unexpected results where we had section 10, which was good as the first result. And then section three was the second result. And that was really unexpected. We want that second result to be software engineering. So when we now run this hybrid approach that combines together multiple different indexes, my hope is that we're going to get first section 10 and then whatever section the software engineering one is. I think it's section two. So let's test this out inside of our new notebook. I'm going to go down to the bottom. And I'll do a results is retriever, search what happened with incident 2023 Q4011. And I'm going to get the first three search results. And then once again, I'm going to print them all out like so. And I'll do the score, a new line, the content of the document, but just the first 200 lines. and then just a little separator between each chunk. So I'm going to run this. And now we get, hey, some much better search results than what we had before. So I've got section 10, and then section 2, exactly what we wanted. And then section 5, but that one's not super relevant here. So we now have a much better output by combining together these two different search techniques And the nice thing about this is we were able to author each of these indexes kind of in isolation. They're their own separate classes. And because we made each implementation have the same exact API with that search function and the add document function, we were able to easily wrap them up into this larger retriever class. So if you wanted to, we could absolutely add in some additional search index here that maybe implements some other completely different searching functionality. And as long as it has that search function and the add document function, We can very easily add it, have it generate some results, and then merge the results along with the results coming from the other search methodologies as well. Okay, so let's say this is a good success, but we're not quite done yet. There's still some other techniques that we're going to go over to improve the accuracy of our rag pipeline.

---

## 🎬 トランスクリプト（日本語）

セマンティック検索の実装ができました。 そして、辞書検索の実装も。これで これらの機能を連携させる必要があります。その方法を説明します。 まず最初に注意してほしいのは、 これら両方の検索機能の実装が ほぼ同じパブリックAPIを持っているということです。 左側にはベクトルインデックスクラスがあり、 ドキュメントの追加や検索といったメソッドがあります。 そして、BM25インデックス内にも ほぼ同じメソッドがあります。そこで、これら2つを 単一の検索パイプラインに接続するために、 「リトリーバー」と呼ぶ新しいクラスでラップします。 このリトリーバーはユーザーの質問を受け取り、 それをベクトルインデックスとBM25インデックスの 検索メソッドに転送します。リトリーバーは 両方から結果を受け取り、結果を マージする方法を見つけます。さて、 このマージ処理は実は少し トリッキーです。そのため、これらの異なる検索方法から 得られる結果をマージする方法について、 詳しく見ていきたいと思います。結果を結合するために、 逆順位融合というテクニックを使用します。 このテクニックを理解する最も簡単な方法は、 例を通して見ることです。では、今すぐそうしましょう。 ベクトルインデックスで検索を実行し、 結果としてセクション27と 6が得られたとします。そして、同じ検索を BM25でも実行し、結果として6、2、 7が得られたとします。これで、この2つの 結果リストを取得し、何らかの方法で結合する必要があります。 そうするために、すべての検索結果をまとめて 単一のテーブルに配置します。このように。 これで、テキストチャンク27と6があり、 ベクトルインデックスの出力からの順位と BM25インデックスの出力からの順位を記録しました。 順位について話すとき、私は単に 検索出力の順位を意味しています。つまり、順位1、 2、3、順位1、2、3。私は単にこれらの 同じ数値を下の表に記載しています。 すべての順位を配置したら、次に数式を適用します。 これが正確な数式です。とてもひどく見えるかもしれませんが、 心配しないでください。それほど複雑ではありません。 仕組みはこうです。各順位の列に対して、 例えばこの列やこの列について、 別の項を記述します。したがって、 最初の項はこちらで、2番目の項はこちらです。 最初の項では、1プラス そこにある数字を1で割ったものを記述します。 つまり、1プラス1の1になります。 そして、2番目の項は1プラス そこにある数字を1で割ったものになります。 つまり、1プラス2の1です。 各テキストチャンクのスコアを計算したら、 テーブルをスコアの大きい順に並べ替えます。 したがって、このようになります。 セクション2のテキストチャンクが 最も関連性の高い検索結果となります。 セクション6は2番目に、 セクション7は最も関連性の低い結果となります。そしてこれは 理にかなっています。個々の検索結果を 見れば、これらの出力が理にかなっていることを視覚的に確認できます。 セクション2は順位1と2でした。つまり、 全体的に、上位に向かっているということです。 セクション6は1と3です。これは 中間くらいです。良いスコアと悪いスコアがあります。そして セクション7は2と3です。したがって、下位に 向かっています。視覚的な検査により、 結果は妥当なものだと思います。 さて、結果をどのように結合するか理解したので、 Jupyter Notebookに戻り、 リトリーバークラスのサンプル実装と 結果のマージのサンプル実装を見てみましょう。 さて、こちらに戻ってきました。次のノートブックに移動します。 005ハイブリッドです。ここでも多くのセットアップがあります。 ベクトルデータベースの実装、VM25の実装、 そして今、リトリーバークラスの実装を追加しました。 リトリーバーにはドキュメント追加メソッドがあります。 ドキュメント追加を呼び出すと、 渡されたドキュメントをリトリーバー内の 各インデックスに渡すだけです。私たちの場合は、インデックスは ベクトルインデックスとBM25インデックスです。 そして、リトリーバーには検索関数もあります。 クエリテキストを渡すと、その クエリテキストはリトリーバー内の各インデックスに 渡されます。次に、すべての結果を取得し、 それらを結合します。ここで、 逆順位融合を実装するマージロジックがあります。 さて、ここで少しテストしてみましょう。 このすべてを始めたきっかけを思い出してください。 ベクトルデータベースの実装に戻りましょう。 このノートブックでは、例えば、 「インシデント2023で何が起こったか」のような ものを検索したときに、予期しない結果が得られました。 セクション10が良い最初の結果として得られましたが、 セクション3が2番目の結果でした。これは非常に 予期せぬことでした。2番目の結果は ソフトウェアエンジニアリングであってほしいです。そこで、複数の 異なるインデックスを組み合わせるこのハイブリッドアプローチを実行すると、 セクション10、次にソフトウェアエンジニアリングの セクションが得られることを期待しています。 おそらくセクション2でしょう。新しいノートブックで試してみましょう。 下の方に移動して、 `results = retriever.search("what happened with` `incident 2023 Q4011")` 最初の3つの検索結果を取得します。 そして、もう一度、すべてをこのように表示します。 スコア、改行、ドキュメントのコンテンツですが、最初の200行だけです。 そして、チャンクごとに簡単な区切りを入れます。 これを実行します。すると、 以前よりもはるかに良い検索結果が得られました。 セクション10、そしてセクション2です。まさに 求めていた通りです。そしてセクション5ですが、これは ここではそれほど関連性が高くありません。 これで、これら2つの異なる検索技術を 組み合わせることで、はるかに良い出力を得ることができました。 そして、良い点は、これらのインデックスをそれぞれ 単独で作成できたことです。それらは独立したクラスです。 そして、各実装が同じAPI、 つまり検索関数とドキュメント追加関数を持つようにしたため、 これらをこの大きなリトリーバークラスに 簡単にラップすることができました。もしあなたが望むなら、 全く異なる検索機能を持つ別の検索インデックスを 追加することも可能です。 そして、それが検索関数とドキュメント追加関数を持っていれば、 それを非常に簡単に、結果を生成させ、 そして他の検索方法からの結果とマージさせることができます。 さて、これは成功と言えますが、まだ終わりではありません。 精度を向上させるために、まだいくつか 技術を学ぶ必要があります。 それは私たちのRAGパイプラインの精度を向上させるためです。
