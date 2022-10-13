package com.javawithspring.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.javawithspring.models.Person;

@Repository
public interface PersonRepository extends JpaRepository<Person, Long>{

}
