import { Component, OnInit } from '@angular/core';
import { ExplorerApiService } from '../services/explorer-api.service'
import { Subscription } from 'rxjs/Subscription';
import { Subscriber } from 'rxjs/Subscriber';
@Component({
  selector: 'app-book-explorer',
  templateUrl: './book-explorer.component.html',
  styleUrls: ['./book-explorer.component.scss']
})
export class BookExplorerComponent implements OnInit {


  // variables
  public entities : Array<string>;
  public terms : Array<{term : string, strength : number}>
  public bookTitles : Array<string>;
  public topics : Array<{id: string, pct: number}>
  public selectedEntity : string = 'Select an Entity';
  public selectedBook : string = 'select a book';
  public topicIDs : Array<number> = [];
  public topicTerms: Array<{topic_id: number, terms : Array<{term: string, strength: number}>}> = [];
  public entityTopics: Array<{topicID : number, pct : number}> =[];


  // subscriptions
  private entitySubscription : Subscription;
  private entityTermSubscription : Subscription;
  private bookTitleSubscription : Subscription;
  private bookTopicSubscription : Subscription
  private topicIDSubscription: Subscription;
  private topicTermSubscriptions: Array<Subscription> = [];

  constructor(public bookQuery : ExplorerApiService) { }

  public requestEntityTerms(entity: string) {
    if(this.entityTermSubscription) {
      this.entityTermSubscription.unsubscribe();
    }
    this.entityTermSubscription = this.bookQuery.requestEntityTerms(this.selectedBook, entity).subscribe((res) => {
      this.selectedEntity = entity;
      this.terms = res.terms;
      this.mapEntityTermTopics()
    });
  }

  public requestEntities(bookTitle: string) {
    this.selectedBook = bookTitle;
    this.entitySubscription = this.bookQuery.requestEntities(bookTitle).subscribe((res) => {
      this.entities = res.entities;
    })
  }

  public mapEntityTermTopics() {
    console.log(this.terms);
    console.log(this.topicTerms);
    let entityTerms = this.terms.map((t) => t.term.toLowerCase());
    let presentTerms = this.topicTerms.map((topic) => {
      return {
        topicID: topic.topic_id,
        terms : topic.terms.filter((term) => entityTerms.indexOf(term.term.toLowerCase()) > -1 )
      }
    });
    console.log('Present Terms')
    console.log(presentTerms);
    let topicScores = presentTerms.map((t) => {
      return {topicID : t.topicID, score : t.terms.reduce((a,b) => a + b.strength, 0)}
    });
    console.log('Topic Scores');
    console.log(topicScores);

    let sum = topicScores.reduce((a,b) => a + b.score, 0);
    this.entityTopics = topicScores.map((t) => {
      return {topicID : t.topicID, pct : t.score/sum }
    });
    console.log('Entity Topics')
    console.log(this.entityTopics)
}

  public requestTopics(bookTitle: string) {
    if(this.bookTopicSubscription) {
      this.bookTopicSubscription.unsubscribe();
    }
    
    this.bookTopicSubscription = this.bookQuery.requestBookTopics(bookTitle).subscribe((res) => {
      let api_topics = res.topics;
      let sum = api_topics.reduce((a,b) => a + b.score, 0); 
      this.topics = api_topics.map((t) => {
        return {id: 'Topic ' + t.topic_id.toString(), pct: (t.score/sum*100).toFixed(2)}
      }).sort((a,b) => b.pct - a.pct);
    });
  }

  public requestTopicIDs() {
    if(this.topicIDSubscription) {
      this.topicIDSubscription.unsubscribe()
    }
    this.topicIDSubscription = this.bookQuery.requestTopicIDs().subscribe((res) => {
      this.topicIDs = res.topic_ids;
      this.topicTermSubscriptions.length = this.topicIDs.length;
      this.topicTerms.length = this.requestTopicIDs.length;
      this.topicIDs.forEach((id) => this.requestTopicTerm(id));
    });
  }

  public requestTopicTerm(topicID) {
    if (this.topicTermSubscriptions[topicID]) {
      this.topicTermSubscriptions[topicID].unsubscribe()
    }
    this.topicTermSubscriptions[topicID] = this.bookQuery.requestTopicTerms(topicID).subscribe((res) => {
      this.topicTerms[topicID] = res;
    });
    console.log(this.topicTerms);
  }
  


  ngOnInit() {
    this.bookTitleSubscription = this.bookQuery.requestBookTitles().subscribe((res) => {
      this.bookTitles = res.books;
    });
    this.requestTopicIDs();
  }

}
