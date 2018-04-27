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
  public selectedEntity : string = 'Select an Entity';
  public selectedBook : string = 'select a book';

  public entities : Array<string>;
  public filteredEntities : Array<string> = [];
  public terms : Array<{term : string, strength : number}>
  public bookTitles : Array<string>;
  public filteredBookTitles : Array<string> = [];

  public topics : Array<{id: string, pct: number}>
  public topicIDs : Array<number> = [];
  public topicTerms: Array<{topic_id: number, terms : Array<{term: string, strength: number}>}> = [];
  
  public entityTopics: Array<{topicID : number, pct : string}> =[];

  public trackedEntities : Array<{name: string, book : string, topics : Array<{topicID: number, pct : string}>}> = [];

  public entitySearch : string = '';
  public bookSearch : string = '';

  // subscriptions
  private entitySubscription : Subscription;
  private entityTermSubscription : Subscription;
  private bookTitleSubscription : Subscription;
  private bookTopicSubscription : Subscription
  private topicIDSubscription: Subscription;
  private topicTermSubscriptions: Array<Subscription> = [];
  private entityTopicSubscription;

  constructor(public bookQuery : ExplorerApiService) {

  }

  public filterEntities() {
    if(this.entitySearch === '') {
      this.filteredEntities = this.entities;
      return;
    }
    this.filteredEntities = this.entities.filter((e) => e.toLocaleLowerCase().includes(this.entitySearch.toLocaleLowerCase()));
  }
  public filterBookTitles() {
    this.filteredBookTitles = this.bookTitles.filter((b) => b.toLocaleLowerCase().includes(this.bookSearch.toLocaleLowerCase()))
  }

  public requestEntityTerms(entity: string, track : boolean = false) {
    if(this.entityTermSubscription) {
      this.entityTermSubscription.unsubscribe();
    }
    if(this.entityTopicSubscription) {
      this.entityTopicSubscription.unsubscribe();
    }

    this.entityTermSubscription = this.bookQuery.requestEntityTerms(this.selectedBook, entity).subscribe((res) => {
      this.selectedEntity = entity;
      this.terms = res.terms;
    });

    this.entityTopicSubscription = this.bookQuery.requestEntityTopics(this.selectedBook, entity).subscribe((res) => {
      this.trackEntityTopics(track)
      this.mapEntityTermTopics(res);      
    });
  }

  public requestEntities(bookTitle: string) {
    this.selectedBook = bookTitle;
    this.selectedEntity = '';
    this.terms = [];
    this.entityTopics = [];
    this.entitySubscription = this.bookQuery.requestEntities(bookTitle).subscribe((res : {entities : string[]}) => {
      this.entities = res.entities.sort();
      this.filterEntities();
    })
  }
  public trackEntityTopics(track: boolean = false) {    
    if(track) {
      this.trackedEntities.push({
        name: this.selectedEntity,
        book : this.selectedBook,
        topics : this.entityTopics
      });
    }
  }
  
  public mapEntityTermTopics(topics : {topics : Array<{entity: string, book:string, topicID:number, strength:number}>}) {

    this.entityTopics = topics.topics.map((t) => {
      return {topicID : t.topicID, pct : t.strength.toFixed(2)}
    });
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
      });//.sort((a,b) => b.pct - a.pct);
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
  
  public trackEntity(name : string) {
    this.requestEntityTerms(name, true);
  }
  public untrackEntity(
    entity : {
      name : string,
      book : string,
      topics : {
        topicID : number,
        pct : string
      }[]}
    ) {
    this.trackedEntities = this.trackedEntities.filter((e) => {
      return e.name != entity.name ||
      e.book != entity.book ||
      !e.topics.every((t, i) => {
        return t.pct == entity.topics[i].pct
         && t.topicID == entity.topics[i].topicID;
      });
    });
  }

  ngOnInit() {
    this.bookTitleSubscription = this.bookQuery.requestBookTitles().subscribe((res :{ books : string[]}) => {
      this.bookTitles = res.books.sort();
      this.filterBookTitles();
    });
    this.requestTopicIDs();
  }

}
