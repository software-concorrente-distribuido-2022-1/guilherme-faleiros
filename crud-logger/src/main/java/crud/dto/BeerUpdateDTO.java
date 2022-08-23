package crud.dto;

import java.math.BigDecimal;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class BeerUpdateDTO {
    private Long id;
    private String name;
    private BigDecimal price;
}
